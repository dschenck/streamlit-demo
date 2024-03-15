# About

Demo [streamlit](https://streamlit-demo-yg4s.onrender.com/) application

## Demo

A live version of the app is hosted on [render.com](http://render.com/) at the following [link](https://streamlit-demo-yg4s.onrender.com/).

> Please note the app may require up to 30 seconds warm-up when called for the first time in a while.

## Test locally

Step 1: close the repository

```
git clone https://github.com/dschenck/streamlit-demo.git
```

Step 2: install dependencies

```
pip install -r requirements.txt
```

Step 3 (optional): get an API key from the [USDA](https://apps.fas.usda.gov/opendataweb/home) (to request the chart data) and set it as an environment variable in the command line

```
SET APIKEY=d96d.....
```

Step 4: launch streamlit local server

```
streamlit run main.py
```
