import streamlit as st
import plotly.express as px
from apirequest import get_data

st.title("Weather Forecast Dashboard")
place = st.text_input("Enter a location (city or country):")
days = st.slider("Select number of days for forecast:",min_value=1, max_value=5, value=3,
                 help="Choose how many days of weather forecast you want to see.")
option = st.selectbox("Select data to view:", options=["Temperature", "Sky"])

st.subheader(f"{option} for the next {days} days in the {place}")

# Creating a chart now
if place:
    d, t = get_data(place, days, option)

    if option == "Temperature":
        print("Plotting Temperature Data")
        figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (°C)"}, title="Temperature Trend")
        st.plotly_chart(figure)
    elif option == "Sky":
        st.image()
