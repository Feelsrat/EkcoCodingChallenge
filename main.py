from location import Location

location = Location()

is_on = True

while is_on:
    try:
        a = input("Input the name of a city or type exit to stop program: ").upper()

        if a == "EXIT":
            exit()

        location.setlocation(a)  # https://geocode.xyz/{locationname}?json=1
        print(a + " is located at: " + location.getlatitude() + " " + location.getlongitude())

        forecast = location.getforecast()  # https://api.openmeteo.com/v1/forecast?latitude=[latt]&longitude=[
    # long]&hourly=temperature_2m

        for x, y in zip(forecast['time'], forecast['temperature_2m']):  # fpr loop to print display time/temperature
            print("Time: " + str(x) + ". Temp: " + str(y) + "°C")

    except:
        print("Location unsupported, please check for typo")
