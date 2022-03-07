import requests


class Location:
    def __init__(self):
        self.latitude = None
        self.longitude = None

    def setlocation(self, locationname):  # Method calls geocode API to return a json object, sometimes cloudflare will
        # trigger causing an error 403, might take a few tries.

        geocodeapi = f"https://geocode.xyz/{locationname}?json=1"
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}
        # Tried to spoof browser with headers as above to no tangible benefit

        response = requests.get(geocodeapi)  # Blocking request, will wait for response
        if response.status_code > 200:
            print(f"Failed API call: {response.status_code} \nTry again")
            self.setlocation(locationname)  # Will call function recursively to bypass error 403
        else:
            responseObj = response.json()

            self.longitude = responseObj['longt']
            self.latitude = responseObj['latt']

            print("Successfully grabbed long & lat")

    def getforecast(self):
        openmeteoapi = f'https://api.open-meteo.com/v1/forecast?latitude={self.getlatitude()}&longitude={self.longitude}&hourly=temperature_2m'

        response = requests.get(openmeteoapi)
        if response.status_code > 200:
            print(f"Failed API call: {response.status_code} \nTry again")
            self.getforecast()  # calls method recursively till a non error response is received
        obj = response.json()
        return obj['hourly'] # returns only the hourly data

    def getlongitude(self):
        return self.longitude

    def getlatitude(self):
        return self.latitude
