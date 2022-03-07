from location import Location


def displayWeather(fcast):
    for x, y in zip(fcast['time'], fcast['temperature_2m']):  # fpr loop to print display time/temperature
        datetime = str(x)
        temp = str(y)

        print("Time: " + datetime.replace("T", " ") + " Temp: " + temp + "°C")


location = Location()

is_on = True

while is_on:
    try:
        a = input("Input the name of a city: ").upper()

        if a == "":
            raise Exception("No city selected!")

        location.setlocation(a)  # https://geocode.xyz/{locationname}?json=1
        print(a + " is located at: " + location.getlatitude() + " " + location.getlongitude())

        forecast = location.getforecast()  # https://api.openmeteo.com/v1/forecast?latitude=[latt]&longitude=[
        # long]&hourly=temperature_2m

        displayWeather(forecast)


    except Exception as e:
        print(e)
