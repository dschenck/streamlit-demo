import streamlit as st
import os

st.title("Code")
st.text("The widget on the home page is generated using the below code")

with open(os.path.join(os.path.dirname(__file__), "../main.py"), "r") as file:
    st.code(file.read())
