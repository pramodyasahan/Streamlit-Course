import streamlit as st
import pandas as pd

st.title("Streamlit From Demo")

with st.form(key="sample_form"):

    st.subheader("Text Input")
    name = st.text_input("Enter your name", placeholder="Enter your name")
    feedback = st.text_area("Provide your feedback")
    st.divider()

    st.subheader("Date and Time Inputs")
    dob = st.date_input("Select your date of birth")
    time = st.text_input("Choose a preferred time")
    st.divider()

    st.subheader("Selectors")
    choice = st.radio("Choose an option", ['Option 1', 'Option 2', 'Option 3'])
    gender = st.selectbox("Select your gender", ['Male', 'Female', 'Other'])
    slider = st.select_slider("Select a range", options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    st.divider()

    st.subheader("Toggles & Checkboxes")
    notifications = st.checkbox("Receive notifications")
    toggle_value = st.checkbox("Enable dark mode?", value=False)
    st.divider()

    submit_button = st.form_submit_button("Submit")

st.subheader("Buttons")


