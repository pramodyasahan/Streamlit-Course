import streamlit as st

file_path = "example.txt"

@st.cache_resource
def get_file_handler():
    return open(file_path, "a+")

try:
    file_handler = get_file_handler()

    if st.button("Write to file"):
        try:
            file_handler.write("New line of text\n")
            file_handler.flush()
            st.success("Write a new line of text")
        except Exception as e:
            st.error(f"Error writing to file: {e}")

    if st.button("Read from file"):
        try:
            file_handler.seek(0)
            content = file_handler.read()
            if content:
                st.write(content)
            else:
                st.info("File is empty")
        except Exception as e:
            st.error(f"Error reading from file: {e}")

except Exception as e:
    st.error(f"Error opening file: {e}")
