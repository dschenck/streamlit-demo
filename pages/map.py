import streamlit as st
import easychart
import easychart.rendering
import requests

st.title("Highcharts map")
st.markdown(
    "Demo on how to use `easychart` with an optional module (e.g. map, sanskey...)"
)

st.info(
    """
    Make sure to add the relevant script in the `easychart.config.scripts`

    ```python
    >>> import easychart
    >>> MODULE = "https://code.highcharts.com/maps/modules/map.js"

    >>> if MODULE not in easychart.config.scripts:
    ...     easychart.config.scripts.append(MODULE)
    ```
    """
)


MODULE = "https://code.highcharts.com/maps/modules/map.js"

if MODULE not in easychart.config.scripts:
    easychart.config.scripts.append(MODULE)

# load the map
# see collection here https://code.highcharts.com/mapdata/
topo = requests.get(
    "https://code.highcharts.com/mapdata/countries/fr/fr-all.topo.json"
).json()

# data
data = [
    ["fr-cor", 10],
    ["fr-bre", 11],
    ["fr-pdl", 12],
    ["fr-pac", 13],
    ["fr-occ", 14],
    ["fr-naq", 15],
    ["fr-bfc", 16],
    ["fr-cvl", 17],
    ["fr-idf", 18],
    ["fr-hdf", 19],
    ["fr-ara", 20],
    ["fr-ges", 21],
    ["fr-nor", 22],
    ["fr-lre", 23],
    ["fr-may", 24],
    ["fr-gf", 25],
    ["fr-mq", 26],
    ["fr-gua", 27],
]

chart = easychart.new("map", cAxis="rdbu")
chart.title = "France"
chart.subtitle = "By region"
chart.chart.map = topo
chart.plot(data, joinBy="hc-key")

st.components.v1.html(easychart.rendering.render(chart), height=400)
