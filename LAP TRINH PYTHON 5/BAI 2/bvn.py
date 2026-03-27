import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dự án Biểu diễn Dữ liệu", layout="wide")
st.title("📊 Website Biểu diễn Dữ liệu")

file_path = "data_lesson2_none_header.csv"

try:
    column_names = ['Thời gian', 'Nội dung', 'Địa điểm', 'Cảm xúc']
    df = pd.read_csv(file_path, header=None, names=column_names)

    st.subheader("1. Hiển thị bằng lệnh `st.write`")
    st.write(df)

    st.divider()

    st.subheader("2. Hiển thị bằng lệnh `st.table` (Bảng tĩnh)")
    st.table(df)

    st.divider()

    st.subheader("3. Hiển thị bằng lệnh `st.dataframe` (Bảng tương tác)")
    st.dataframe(df, use_container_width=True)

except FileNotFoundError:
    st.error(f"Không tìm thấy file '{file_path}'. Hãy kiểm tra lại tên file.")
except Exception as e:
    st.error(f"Lỗi: {e}")