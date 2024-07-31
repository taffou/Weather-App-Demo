# ? - importing necessary modules

import welcome_msg as wmsg
import fetch_data as fd
# import subprocess as sup

# Formatting Variables

format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")


def main():
# ? 1- Welcome message
# * Welcome the user 
    wmsg.welcome()

# ? 2- Fetching Weather Data 
    # city = sup.run([input("Enter a city name!")], stdout=sup.PIPE, text=True)
    city = input("Enter a city name!")
    # fd.weather_info()

# ? 3- Display Weather Data
# * Display Data by requested city
    # fd.weather_city(city.capitalize())
    fd.weather_city(city.title())

if __name__ == "__main__":
    main()


















# Formatted Message - Signify END of Output
print(f"{format_output}---END---{format_reset}")
