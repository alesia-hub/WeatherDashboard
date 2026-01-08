'''
Module to handle API requests for weather data.
'''
import requests

API_KEY = "3cce2f035bbfa7e92b582fbcbc7f7928"

def get_data(place, days, kind="Temperature"):
    # This function would normally fetch data from a weather API.
    print("Executing First API:")
    geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={place}&limit=5&appid={API_KEY}"
    # getting lat lon coordinates by place name
    geocoding_response = requests.get(geocoding_url, timeout=5)
    print(geocoding_response.url)
    print(geocoding_response.status_code)
    geocoding_data = geocoding_response.json()
    print(geocoding_data)

    if len(geocoding_data) <1:
        return None, None
    else:
        lat = geocoding_data[0]["lat"]
        lon = geocoding_data[0]["lon"]
        print("Received results for coordinates: ", geocoding_data[0]["lat"], geocoding_data[0]["lon"])
        

        weather_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
        weather_request = requests.get(weather_url, timeout=5)
        weather_data = weather_request.json()
        # print("Weather response: ", weather_data['list'][0])
        list_data = weather_data['list']
        # Selecting only data for the given number of days: 
        forecast_data = list_data[:days*8]  # 8 data points per day (3-hour intervals)

        if kind == "Temperature":
            dispaly_temp  = [temp['main']['temp'] for temp in forecast_data] # contains temp per hour for given number of days
            #print("Temperature data: ", dispaly_temp)
            display_dates = [dt['dt_txt'] for dt in forecast_data]
            #print("Dates to display  ", display_dates)
            return display_dates, dispaly_temp
        elif kind == "Sky":
            sky_conditions = [sky['weather'][0]['description'] for sky in forecast_data]
            print("Sky conditions: ", sky_conditions)
            display_dates = [dt['dt_txt'] for dt in forecast_data]
            return display_dates, sky_conditions


if __name__ == "__main__":
    d, t = get_data("London", 3, kind="Sky")
    print(d, t)