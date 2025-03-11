import os
import pandas as pd
import streamlit as st

st.title("This is a Title")
st.header("This is a Header")
st.subheader("This is a Subheader")
st.markdown("This is a _Markdown_")
st.caption("This is a **Caption**")
code = """
def greet(name):
    print("Hello " + name)
"""
st.code(code, language="python")
st.divider()

st.image(os.path.join(os.getcwd(), "static", "BG.jpg"))
st.divider()

st.title("Streamlit Element Demo")

st.subheader("Dataframe")
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [42, 32, 47, 29],
    'Occupation': ["Engineer", "Doctor", "Lawyer", "Teacher"]
})
st.dataframe(df)
st.subheader("Data Editor")
editor = st.data_editor(df)

st.subheader("Static Table")
st.table(df)
st.divider()

st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df["Age"].mean(), 2))
st.divider()

st.subheader("JSON and Dictionary")
sample_data = {
    'Name': "Alice",
    'Age': 42,
    'Skills': ['Python', 'Java', "Machine Learning"],
}
st.json(sample_data)
st.caption("Dictionary")
st.write(sample_data)
