# - Fetch weather data

# ? Importing module called data 

import data as d

# * Fetching and displaying the whole weather dataset
def weather_info():
    for data in d.weather_data:
        print(d.weather_data[data])

def weather_city(city):
    # * Stripping the parameter string from leading and trailing space
    c_city = city.strip()
    
    match c_city:
            case "London":
                print(f'Weather in {c_city} -- {d.weather_data[c_city]}')
                return True
            case "New York":
                print(f'Weather in {c_city} -- {d.weather_data[c_city]}')
                return True
            case "Tokyo":
                print(f'Weather in {c_city} -- {d.weather_data[c_city]}')
                return True
            case "Sydney":
                print(f'Weather in {c_city} -- {d.weather_data[c_city]}')
                return True
            case "Paris":
                print(f'Weather in {c_city} -- {d.weather_data[c_city]}')
                return True
            case _:
                print("Invalid City!")
                return False



