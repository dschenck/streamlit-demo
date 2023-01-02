import streamlit as st

st.title("Hello world!")

x = st.slider("Select value", key="x")

st.write(x, "squared is", x * x)

