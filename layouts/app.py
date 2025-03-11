import streamlit as st

st.sidebar.title("This is the Sidebar")
st.sidebar.write("You can place elements like sliders, buttons, and text here")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

tab1, tab2, tab3 = st.tabs(['Tab1', 'Tab2', 'Tab3'])

with tab1:
    st.write("You are in Tab 1")
with tab2:
    st.write("You are in Tab 2")
with tab3:
    st.write("You are in Tab 3")
st.divider()


col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.header("Column 2")
    st.write("Content for column 2")


with st.container(border=True):
    st.write("This is inside the container")
    st.write("You can think of containers as a grouping for elements.")
    st.write("Containers help manage sections of the page.")


placeholder = st.empty()
placeholder.write("This is an empty placeholder, useful for dynamic content.")

if st.button("Update Placeholder"):
    placeholder.write("The content of this placeholder has been updated.")

with st.expander("Expand for more details"):
    st.write("This is additional information about this page.")
    st.write("You can use expanders to keep your interface cleaner")

st.write("Hover over this button for a tooltip")
st.button("Button with a tooltip", help="This is a tooltip or popover on hover.")

if sidebar_input:
    st.write(f"You entered in the sidebar {sidebar_input}.")
