import streamlit as st
import pandas as pd

st.title("Phân tích dữ liệu bất động sản")

uploaded_file = st.file_uploader("Tải file CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Làm sạch
    df = df.drop_duplicates()
    df = df.dropna()

    st.subheader("Dữ liệu sau làm sạch")
    st.dataframe(df)

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_cols) > 0:
        selected_col = st.selectbox("Chọn cột số", numeric_cols)

        st.subheader("Biểu đồ phân bố")

        chart = {
            "mark": "bar",
            "encoding": {
                "x": {
                    "bin": True,
                    "field": selected_col,
                    "type": "quantitative"
                },
                "y": {
                    "aggregate": "count",
                    "type": "quantitative"
                }
            }
        }

        st.vega_lite_chart(df, chart, use_container_width=True)

        st.subheader("Kết quả phân tích")
        st.write("Trung bình:", df[selected_col].mean())
        st.write("Lớn nhất:", df[selected_col].max())
        st.write("Nhỏ nhất:", df[selected_col].min())