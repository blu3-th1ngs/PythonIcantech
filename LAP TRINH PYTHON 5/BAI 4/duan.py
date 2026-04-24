import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quản Lý Điểm Học Sinh", layout="centered")

st.title("Quản Lý Điểm Học Sinh")
st.subheader("Bảng điểm hiện tại")

if 'df' not in st.session_state:
    data = {
        'Tên': ['Trung', 'Hoàng', 'Trang', 'Lan', 'Minh', 'Hà', 'Phúc', 'An', 'Mai', 'Quân'],
        'Toán': [3, 6, 8, 9, 5, 7, 10, 4, 6, 8],
        'Văn': [8, 5, 9, 7, 6, 8, 9, 5, 7, 6],
        'Anh': [7, 8, 9, 10, 4, 6, 8, 6, 9, 7]
    }
    st.session_state.df = pd.DataFrame(data)

df = st.session_state.df

st.dataframe(df, use_container_width=True, hide_index=False)

st.markdown("### <span style='color:#9b59b6;'>+</span> Thêm học sinh mới", unsafe_allow_html=True)

col_ten, _ = st.columns([3, 1])
ten_hoc_sinh = col_ten.text_input("Tên học sinh", placeholder="Nhập tên học sinh mới", key="ten_input")

st.subheader("Điểm Toán")
diem_toan = st.number_input("", min_value=0, max_value=10, value=0, step=1, key="toan_input", label_visibility="collapsed")

st.subheader("Điểm Văn")
diem_van = st.number_input("", min_value=0, max_value=10, value=0, step=1, key="van_input", label_visibility="collapsed")

st.subheader("Điểm Anh")
diem_anh = st.number_input("", min_value=0, max_value=10, value=0, step=1, key="anh_input", label_visibility="collapsed")

if st.button("Thêm học sinh", type="primary", use_container_width=True):
    if ten_hoc_sinh.strip() == "":
        st.error("Vui lòng nhập tên học sinh!")
    else:
        new_row = pd.DataFrame({
            'Tên': [ten_hoc_sinh.strip()],
            'Toán': [diem_toan],
            'Văn': [diem_van],
            'Anh': [diem_anh]
        })
        df_copy = df.copy()
        df_moi = df_copy._append(new_row, ignore_index=True)
        st.session_state.df = df_moi
        st.success(f"✅ Đã thêm học sinh **{ten_hoc_sinh}** thành công!")
        st.rerun()

st.markdown("---")
st.subheader("🏆 Top 3 học sinh có điểm Toán cao nhất")

top3 = df.nlargest(3, 'Toán')
st.dataframe(top3, use_container_width=True, hide_index=False)

st.caption(f"Điểm Toán cao nhất: **{df['Toán'].max()}** | Thấp nhất: **{df['Toán'].min()}**")

st.subheader("📊 Biểu đồ Top 3 Toán (Vega Lite)")

vega_spec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "data": {"values": top3.to_dict(orient="records")},
    "mark": {"type": "bar", "cornerRadiusEnd": 4},
    "encoding": {
        "x": {"field": "Tên", "type": "nominal", "sort": "-y"},
        "y": {"field": "Toán", "type": "quantitative", "title": "Điểm Toán"},
        "color": {"value": "#9b59b6"},
        "tooltip": [{"field": "Tên"}, {"field": "Toán"}]
    },
    "width": 500,
    "height": 300
}
st.vega_lite_chart(vega_spec)