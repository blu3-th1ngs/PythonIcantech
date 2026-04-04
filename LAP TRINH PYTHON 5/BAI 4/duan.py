import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Analysis Project", layout="wide")

st.title("Data Analysis Project")

@st.cache_data
def load_data():
    return pd.read_csv("LAP TRINH PYTHON 5/BAI 4/most-popular_updated_15_feb.csv")

df = load_data()

st.subheader("Dataset")
st.dataframe(df)

st.subheader("Info")
st.write(df.shape)
st.write(df.columns.tolist())

col = st.selectbox("Column", df.columns)

vc = df[col].value_counts().reset_index()
vc.columns = [col, "count"]

st.subheader("Value Counts")
st.dataframe(vc)

st.subheader("Bar Chart")
st.vega_lite_chart(
    vc.head(10),
    {
        "mark": "bar",
        "encoding": {
            "x": {"field": col, "type": "nominal", "sort": "-y"},
            "y": {"field": "count", "type": "quantitative"}
        }
    },
    use_container_width=True
)

st.subheader("Pie Chart")
st.vega_lite_chart(
    vc.head(5),
    {
        "mark": {"type": "arc"},
        "encoding": {
            "theta": {"field": "count", "type": "quantitative"},
            "color": {"field": col, "type": "nominal"}
        }
    },
    use_container_width=True
)

num_cols = df.select_dtypes(include=["int64", "float64"]).columns

if len(num_cols) > 0:
    ncol = st.selectbox("Numeric Column", num_cols)

    st.write(df[ncol].mean())
    st.write(df[ncol].max())
    st.write(df[ncol].min())

    st.subheader("Histogram")
    st.vega_lite_chart(
        df,
        {
            "mark": "bar",
            "encoding": {
                "x": {"field": ncol, "bin": True, "type": "quantitative"},
                "y": {"aggregate": "count", "type": "quantitative"}
            }
        },
        use_container_width=True
    )

search = st.text_input("Search")

if search:
    f = df[df.astype(str).apply(lambda r: r.str.contains(search, case=False).any(), axis=1)]
    st.dataframe(f)