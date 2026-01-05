import streamlit as st

st.title("Weather Forecast Dashboard")
place = st.text_input("Enter a location (city or country):")
days = st.slider("Select number of days for forecast:",min_value=1, max_value=7, value=3,
                 help="Choose how many days of weather forecast you want to see.")
option = st.selectbox("Select data to view:", options=["Temperature", "Sky"])

st.subheader(f"{option} for the next {days} days in the {place}")

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5001, debug=False)