import requests


def get_weather_forecast(api_key, location):
    base_url = "http://api.weatherstack.com/current"  # weatherstack website
    params = {
        "access_key": api_key,
        "query": location,
    }
    response = requests.get(base_url, params=params)
    # print(response.json())

    if response.status_code == 200:  # This checks if the HTTP status code of the response is equal to 200,
        # which typically signifies a successful response.
        data = response.json()
        return data
    else:
        return None


def print_location_details(location_details):
    dict = location_details
    str = "{}, {}, {}, and localtime: {}".format(dict['name'], dict['region'], dict['country'], dict['localtime'])
    print("\n==> The location details :", str)


def print_weather_details(weather):
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("\t\t\t\tTEMPERATURE DETAILS")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    weather_details = (("-> Temperature: {}\n-> Humidity: {}\n-> Precipitation: {}\n-> Wind details:\n\t* Wind Speed:{}\n\t* Wind Direction: {}\n\t* Wind Degree: {}\n-> Description: {}")
                       .format(weather["temperature"], weather['humidity'],
                               weather['precip'], weather["wind_speed"],
                               weather['wind_dir'], weather['wind_degree'],
                               weather["weather_descriptions"], ))
    print(weather_details)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def main():
    print('--------------------------------------------------------')
    print('\t\t\t\tWelcome to WEATHER FORECAST')
    print('--------------------------------------------------------')
    api_key = '2752651cba9497aa4ad2a778f3d362f3'
    location = input("Enter the desired location: ")
    print('--------------------------------------------------------')
    weather_data = get_weather_forecast(api_key, location)

    try:
        if weather_data:
            location_details = weather_data["location"]
            print_location_details(location_details)
            weather_details = weather_data["current"]
            print_weather_details(weather_details)
        else:
            print("Failed to retrieve weather data.")
    except:
        print('Error in fetching the location')
    finally:
        print('\n--------------------------------------------------------')
        print('\t\t\tTHANK YOU FOR USING WEATHER FORECAST')
        print('--------------------------------------------------------')


if __name__ == "__main__":
    main()
