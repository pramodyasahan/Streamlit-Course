import streamlit as st
from datetime import datetime

st.title("User Information Form")

form_value = {
    'name': None,
    'height': None,
    'gender': None,
    'dob': None,
}

min_date = datetime(1950, 1, 1)
max_date = datetime.now()

with st.form(key="user_form"):
    form_value['name'] = st.text_input("Name")
    form_value['height'] = st.number_input("Height")
    form_value['gender'] = st.selectbox("Gender", ["Male", "Female"])
    form_value['dob'] = st.date_input("Date of Birth", min_value=min_date, max_value=max_date)

    submit_button = st.form_submit_button("Submit")
    st.divider()
    if submit_button:
        if not all(form_value.values()):
            st.warning("Please fill all values")
        else:
            st.balloons()
            st.write("### User Information")
            for key, value in form_value.items():
                st.write(f"{key}: {value}")