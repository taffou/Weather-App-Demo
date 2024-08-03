
# Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# * Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")

# ? - importing necessary modules

import data as d
import fetch_data as fd
import messages as msg

def main():
    fd.weather_info()
    try:
        # ? 1.1- Welcome message     
        print("...........................................++++++..............................................")
        # ? 1.2- Welcome message
        msg.welcome()
        print("...........................................++++++..............................................")
        while True:
            # ? 1.3- Fetching Weather Data 
            city = input("Enter a city name!")
            # ? 1.4- Display city weather Data 
            isCity = fd.weather_city(city.title())
            while isCity == False:
                city = input("Enter a valid city name!")
                isCity = fd.weather_city(city.title())
            print("...........................................++++++..............................................")
            user_input = input("Press Any key to continue or \"E\" to exit the App")
            print("....................++++++.....................")
            if user_input.capitalize() == "E":
                msg.goodbye()
                print("...........................................++++++..............................................")
                break
    except Exception as e:
        print(f"An error occured: {e}")
    else:
        print("Accurate App")
    finally: 
        print("Reload...")
        print("...........++++++............")

if __name__ == "__main__":
    main()

# * Formatted Message - Signify END of Output
print(f"{format_output}---END---{format_reset}")