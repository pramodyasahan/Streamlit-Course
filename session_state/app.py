import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter += 1
    st.write(f"Counter: {st.session_state.counter}")

if st.button("Decrement"):
    st.session_state.counter -= 1
    st.write(f"Counter: {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0

st.write("### Session State")
st.write(f"Counter Value: {st.session_state.counter}")