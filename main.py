from location import Location
from location import printdict as pd

print("This program will display hourly temperature data for a selected location for a range of 7 days.")


def inputStr():
    return input("\nInput the name of a city or hit enter to quit: ").upper()


def main():
    location = Location()

    is_on = True

    while is_on:
        try:
            a = inputStr()

            if a == "":
                quit()

            location.geocodeapi(a)  # https://geocode.xyz/{locationname}?json=1
            forecast = location.forecastapi()
            location.getweather(forecast)

            pd(location.forecastdict)

        except Exception as e:
            # print('type is:', e.__class__.__name__)
            print(e)


if __name__ == "__main__":
    main()
