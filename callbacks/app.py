import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}


def go_to_step2(name):
    st.session_state.info["name"] = name
    st.session_state.step = 2


def go_to_step1():
    st.session_state.step = 1


if st.session_state.step == 1:
    st.header("Part 01: Info")
    name = st.text_input("Enter your name", value=st.session_state.info.get("name", ""))

    st.button("Next", on_click=go_to_step2, args=(name,))


elif st.session_state.step == 2:
    st.header("Part 02: Review")

    st.subheader("Please review this:")
    st.write(f"**Name:**: {st.session_state.info.get('name', '')}")

    if st.button("Submit"):
        st.success("Great!")
        st.balloons()
        st.session_state.info = {}

    st.button("Back", on_click=go_to_step1)

