import streamlit as st
import streamlit_highcharts as sh
import easychart
import requests
import os
import pandas as pd

st.title("Hello world!")


def retrieve_data(year, code):
    # make data request
    res = requests.get(
        f"https://apps.fas.usda.gov/OpenData/api/esr/exports/commodityCode/{code}/allCountries/marketYear/{year}",
        headers={"API_KEY": os.environ["APIKEY"]},
    )
    print(code, year)
    assert res.status_code == 200

    # parse data
    data = pd.DataFrame(res.json())

    # sum exports by week
    srs = data.groupby(pd.to_datetime(data["weekEndingDate"]))["weeklyExports"].sum()

    # create chart
    chart = easychart.new("column", datetime=True)
    chart.title = "Exports by week"
    chart.subtitle = (
        "Source: US Departement of Agriculture, Foreign Agriculture Service (FAS)"
    )
    chart.plot(srs, name="Weekly exports")

    # create widget
    return chart.serialize()


year = st.number_input("Enter year", value=2020)
code = st.text_input("Enter code", value=101)

sh.streamlit_highcharts(retrieve_data(year, code))

