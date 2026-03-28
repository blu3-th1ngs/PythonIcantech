import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Data Dashboard", layout="wide")

st.title("📊 Dự án Biểu diễn Dữ liệu")

base_path = os.path.join("LAP TRINH PYTHON 5", "BAI 3")

if os.path.exists(base_path):
    files = [f for f in os.listdir(base_path) if f.endswith('.csv')]
    selected_file = st.sidebar.selectbox("Chọn tệp dữ liệu", files)

    if selected_file:
        file_path = os.path.join(base_path, selected_file)
        df = pd.read_csv(file_path)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("📋 Dữ liệu mẫu")
            st.write(df.head(10))
            
            st.divider()
            columns = df.columns.tolist()
            chart_type = st.radio("Loại biểu đồ", ["bar", "line", "point", "area"])
            x_axis = st.selectbox("Trục X", columns)
            y_axis = st.selectbox("Trục Y", columns)

        with col2:
            st.subheader("📈 Biểu đồ Vega-Lite")
            
            x_type = 'nominal' if df[x_axis].dtype == 'object' else 'quantitative'
            y_type = 'quantitative' if df[y_axis].dtype in ['int64', 'float64'] else 'nominal'
            
            st.vega_lite_chart(df, {
                'mark': {'type': chart_type, 'tooltip': True},
                'encoding': {
                    'x': {'field': x_axis, 'type': x_type},
                    'y': {'field': y_axis, 'type': y_type}
                },
                'width': 'container',
                'height': 400
            })
else:
    st.error(f"Không tìm thấy thư mục: {base_path}")