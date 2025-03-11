import time
import streamlit as st


@st.cache_data(ttl=60)  # Cache this data for 60s
def fetch_data():
    time.sleep(3) # Simulate a slow data fetching process like API calls
    return {"data": "This is cache data!"}


st.write("Fetching data...")
data = fetch_data()
st.write(data)
