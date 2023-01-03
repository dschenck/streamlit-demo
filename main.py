import streamlit as st
import streamlit_highcharts as sh
import easychart

import time


@st.cache
def retrieve_data(i):
    time.sleep(5)
    return [3 + 4 * x + x ** 2 for x in range(int(i))]


st.title("Hello world!")

i = st.number_input("Enter x")


chart = easychart.new()
chart.plot(retrieve_data(i))


sh.streamlit_highcharts(chart.serialize())

