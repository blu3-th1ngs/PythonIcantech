import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Quản Lý Điểm Học Sinh", layout="centered")
st.title("Quản Lý Điểm Học Sinh")

@st.cache_data
def load_data():
    path = os.path.join("students.csv", "BAI 5", "LAP TRINH PYTHON 5")
    try:
        df = pd.read_csv(path)
    except:
        data = {
            'Tên': ['Trung', 'Hoàng', 'Trang', 'Lan', 'Minh', 'Hà', 'Phúc', 'An', 'Mai', 'Quân'],
            'Toán': [3, 6, 8, 9, 5, 7, 10, 4, 6, 8],
            'Văn': [8, 5, 9, 7, 6, 8, 9, 5, 7, 6],
            'Anh': [7, 8, 9, 10, 4, 6, 8, 6, 9, 7]
        }
        df = pd.DataFrame(data)
    return df

if 'df_students' not in st.session_state:
    st.session_state.df_students = load_data()

st.subheader("Bảng điểm hiện tại")
st.dataframe(st.session_state.df_students, use_container_width=True)

st.markdown("### ➕ Thêm học sinh mới")
with st.form("add_student_form"):
    new_name = st.text_input("Tên học sinh")
    col1, col2, col3 = st.columns(3)
    with col1:
        math_score = st.number_input("Điểm Toán", 0.0, 10.0, 0.0)
    with col2:
        literature_score = st.number_input("Điểm Văn", 0.0, 10.0, 0.0)
    with col3:
        english_score = st.number_input("Điểm Anh", 0.0, 10.0, 0.0)
    submit_button = st.form_submit_button("Thêm học sinh")

if submit_button and new_name:
    new_row = pd.DataFrame({'Tên': [new_name], 'Toán': [math_score], 'Văn': [literature_score], 'Anh': [english_score]})
    df_copy = st.session_state.df_students.copy()
    st.session_state.df_students = df_copy._append(new_row, ignore_index=True)
    st.rerun()

st.divider()
st.subheader("📊 Biểu đồ phân tích điểm Toán")

top_3_math = st.session_state.df_students.nlargest(3, 'Toán')

st.vega_lite_chart(st.session_state.df_students, {
    'mark': {'type': 'bar', 'tooltip': True},
    'encoding': {
        'x': {'field': 'Tên', 'type': 'nominal', 'sort': '-y'},
        'y': {'field': 'Toán', 'type': 'quantitative'},
        'color': {
            'condition': {
                'test': f"datum.Toán >= {top_3_math['Toán'].min()}",
                'value': '#ff4b4b'
            },
            'value': '#1f77b4'
        }
    },
    'width': 'container'
})

st.subheader("🏆 Top 3 học sinh điểm Toán cao nhất")
st.table(top_3_math[['Tên', 'Toán']])

col_max, col_min = st.columns(2)
col_max.metric("Điểm Toán cao nhất", st.session_state.df_students['Toán'].max())
col_min.metric("Điểm Toán thấp nhất", st.session_state.df_students['Toán'].min())