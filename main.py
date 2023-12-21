import streamlit as st
import easychart
import easychart.rendering
import requests
import os
import pandas as pd

# this is to ensure the chart takes 100% of the available width
# otherwise it will default to 600px (not responsive)
easychart.config.rendering.responsive = True

st.title("Hello world!")

st.info("This is a demo app")

st.markdown(
    """
    The **Export Sales Reporting Program** monitors U.S. agricultural export sales on a daily and weekly basis. The program requires U.S. exporters to report sales of certain commodities to FAS each week. Commodities currently covered by the program are wheat, wheat products, barley, corn, grain sorghum, oats, rye, rice, soybeans, soybean cake and meal, soybean oil, cotton, cottonseed, cottonseed cake and meal, cottonseed oil, sunflowerseed oil, flaxseed, linseed oil, cattle hides and skins, beef and pork. FAS publishes a weekly summary of export sales activity every Thursday at 8:30 a.m. Eastern time, unless a change is announced.
    """
)


@st.cache_data
def load(year, code):
    """
    Load USDA exports data
    """
    # make data request
    res = requests.get(
        f"https://apps.fas.usda.gov/OpenData/api/esr/exports/commodityCode/{code}/allCountries/marketYear/{year}",
        headers={"API_KEY": os.environ["APIKEY"]},
    )

    if res.status_code != 200:
        raise Exception(
            f"The USDA FAS server responded with code {res.status_code} ({res.text})"
        )

    # parse data
    return pd.DataFrame(res.json())


def render(year, code):
    """
    Render out the USDA data
    """
    # load data
    try:
        data = load(year=year, code=code)
    except Exception as e:
        return st.error(f"**Exception**: {e}")

    # sum exports by week
    srs = data.groupby(pd.to_datetime(data["weekEndingDate"]))["weeklyExports"].sum()

    # create chart
    chart = easychart.new("column", datetime=True, exporting=False)
    chart.title = "US exports by week"
    chart.subtitle = "Source: US Departement of Agriculture (FAS)"
    chart.plot(srs, name="Weekly exports")

    # render widget
    st.components.v1.html(easychart.rendering.render(chart), height=400)

    # create another chart
    chart = easychart.new("line", datetime=True, exporting=False)
    chart.title = "Cumulative exports by week since start of marketing year"
    chart.subtitle = "Source: US Departement of Agriculture (FAS)"
    chart.plot(srs.cumsum(), legend=False, marker=None, name="Cumulative exports")

    st.components.v1.html(easychart.rendering.render(chart), height=400)
    return


columns = st.columns(2)

with columns[0]:
    year = st.selectbox(
        "Select marketing year",
        options=[2019, 2020, 2021, 2022, 2023, 2024],
        index=4,
        format_func=lambda option: f"MY{str(option-1)[-2:]}/{str(option)[-2:]}",
    )

with columns[1]:
    code = st.selectbox(
        "Select commodity",
        options=[107, 801],
        format_func=lambda option: {107: "Wheat", 801: "Soybean"}[option],
    )

render(year=year, code=code)
