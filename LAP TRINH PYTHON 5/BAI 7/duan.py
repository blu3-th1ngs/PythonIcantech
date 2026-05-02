import os
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Dự Án Phân Tích Dữ Liệu Học Sinh", layout="centered")
st.title("Dự Án Phân Tích Dữ Liệu Bảng Điểm Học Sinh")
st.markdown(
    "Ứng dụng này thực hiện cả phân tích mô tả và phân tích chuẩn đoán trên dữ liệu `Số Giờ Học` và `Điểm Số`."
)

@st.cache_data
def load_dataset():
    current_dir = os.path.dirname(__file__)
    fallback_path = os.path.normpath(os.path.join(current_dir, 'data5.8.csv'))

    if os.path.exists(fallback_path):
        df = pd.read_csv(fallback_path)
        df.columns = [col.strip() for col in df.columns]
        if 'Hours' in df.columns and 'Scores' in df.columns:
            df = df.rename(columns={'Hours': 'Số Giờ Học', 'Scores': 'Điểm Số'})
        if 'Số Giờ Học' in df.columns and 'Điểm Số' in df.columns:
            return df

    sample = {
        'Số Giờ Học': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7,
                        7.7, 5.9, 4.5, 3.3, 1.1, 8.9, 2.5, 1.9, 6.1, 7.4,
                        2.7, 4.8, 3.8, 6.9, 7.8],
        'Điểm Số': [21, 47, 27, 75, 30, 20, 88, 60, 81, 25,
                    85, 62, 41, 42, 17, 95, 30, 24, 67, 69,
                    30, 54, 35, 76, 86]
    }
    return pd.DataFrame(sample)

uploaded_file = st.file_uploader("Tải lên file CSV dữ liệu học sinh (có cột Số Giờ Học và Điểm Số)")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.success("Dữ liệu đã được tải lên thành công.")
else:
    data = load_dataset()

if 'Số Giờ Học' not in data.columns or 'Điểm Số' not in data.columns:
    st.error('Dữ liệu phải có hai cột: `Số Giờ Học` và `Điểm Số`. Vui lòng kiểm tra lại file CSV.')
    st.stop()

st.subheader("1. Dữ liệu và phân tích mô tả")
st.dataframe(data, use_container_width=True)

st.markdown("### Thông tin thống kê mô tả")
st.write(data.describe())

corr = data['Số Giờ Học'].corr(data['Điểm Số'])
st.write(f"- Hệ số tương quan giữa Số Giờ Học và Điểm Số: **{corr:.3f}**")

col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Phân bố Số Giờ Học")
    st.bar_chart(data['Số Giờ Học'])
with col2:
    st.markdown("#### Phân bố Điểm Số")
    st.bar_chart(data['Điểm Số'])

st.divider()
st.subheader("2. Phân tích chuẩn đoán")

x = data['Số Giờ Học'].to_numpy()
y = data['Điểm Số'].to_numpy()
coef, intercept = np.polyfit(x, y, 1)
predicted = coef * x + intercept
r2 = 1 - np.sum((y - predicted) ** 2) / np.sum((y - np.mean(y)) ** 2)

data['Điểm Dự Đoán'] = np.round(predicted, 1)
data['Sai Số'] = np.round(data['Điểm Số'] - data['Điểm Dự Đoán'], 1)

def regression_spec(df):
    return {
        'layer': [
            {
                'mark': {'type': 'point', 'filled': True, 'tooltip': True},
                'encoding': {
                    'x': {'field': 'Số Giờ Học', 'type': 'quantitative'},
                    'y': {'field': 'Điểm Số', 'type': 'quantitative'},
                    'color': {'value': '#1f77b4'}
                }
            },
            {
                'mark': {'type': 'line', 'color': 'firebrick'},
                'transform': [{'regression': 'Điểm Số', 'on': 'Số Giờ Học'}],
                'encoding': {
                    'x': {'field': 'Số Giờ Học', 'type': 'quantitative'},
                    'y': {'field': 'Điểm Số', 'type': 'quantitative'}
                }
            }
        ]
    }

st.markdown("### Biểu đồ tương quan và đường hồi quy")
st.vega_lite_chart(data, regression_spec(data), use_container_width=True)

st.markdown("### Mô hình hồi quy dự đoán")
st.write(f"Công thức dự đoán: **Điểm Số = {coef:.2f} × Số Giờ Học + {intercept:.2f}**")
st.write(f"Hệ số xác định R²: **{r2:.3f}**")

st.markdown("### Dữ liệu chuẩn đoán")

col3, col4 = st.columns(2)
with col3:
    st.metric("Điểm dự đoán trung bình", f"{data['Điểm Dự Đoán'].mean():.1f}")
with col4:
    st.metric("Sai số trung bình", f"{data['Sai Số'].abs().mean():.1f}")

st.markdown("#### Các điểm có sai số lớn nhất")
worst = data.reindex(data['Sai Số'].abs().sort_values(ascending=False).index).head(5)
st.table(worst[['Số Giờ Học', 'Điểm Số', 'Điểm Dự Đoán', 'Sai Số']])

st.markdown("### Dự đoán theo số giờ học")
selected_hours = st.slider('Chọn số giờ học', float(data['Số Giờ Học'].min()), float(data['Số Giờ Học'].max()), 5.0, step=0.5)
pred_score = coef * selected_hours + intercept
st.write(f"Dự đoán Điểm Số cho **{selected_hours:.1f} giờ học** là **{pred_score:.1f}** điểm.")

if pred_score >= 80:
    st.success("Dự báo: hiệu quả học tập rất tốt.")
elif pred_score >= 60:
    st.info("Dự báo: kết quả học tập trung bình khá.")
else:
    st.warning("Dự báo: cần tăng số giờ học để cải thiện điểm số.")

st.markdown(
    "---\n"
    "**Giải thích:**\n"
    "- Phân tích mô tả giúp ta thấy phân bố và xu hướng dữ liệu hiện tại.\n"
    "- Phân tích chuẩn đoán sử dụng đường hồi quy để xác định mối quan hệ giữa `Số Giờ Học` và `Điểm Số`.\n"
    "- Sai số giữa điểm thực tế và điểm dự đoán cho biết những điểm nào lệch nhiều so với kỳ vọng."
)
