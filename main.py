from location import Location


def displayWeather(fcast):
    for x, y in zip(fcast['time'], fcast['temperature_2m']):  # for loop printing time/temperature
        datetime = str(x)
        temp = str(y)

        print("Date: " + datetime.replace("T", " Time: ") + " Temp: " + temp + "°C")


location = Location()

is_on = True

print("This program will display hourly temperature data for a selected location for a range of 7 days.")

while is_on:
    try:
        a = input("\nInput the name of a city or hit enter to quit: ").upper()

        if a == "":
            quit()

        location.setlocation(a)  # https://geocode.xyz/{locationname}?json=1
        print(a + " is located at: " + location.getlatitude() + " " + location.getlongitude())

        forecast = location.getforecast()  # https://api.openmeteo.com/v1/forecast?latitude=[latt]&longitude=[
        # long]&hourly=temperature_2m

        displayWeather(forecast)

    except Exception as e:
        print(e)
