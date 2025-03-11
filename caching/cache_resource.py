import streamlit as st

file_path = "example.txt"


@st.cache_resource  # Every user shares the same file
def get_file_handler():
    file = open(file_path, "a+")
    return file


file_handler = get_file_handler()

if st.button("Write to file"):
    file_handler.write("New line of text\n")
    file_handler.flush()  # Ensure the content is written immediately
    st.success("Write a new line of text")

if st.button("Read from file"):
    file_handler.seek(0)  # Move to the beginning of the file
    content = file_handler.read()
    st.write(content)

st.button("Close File", on_click=file_handler.close)
