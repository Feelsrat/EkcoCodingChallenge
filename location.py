import requests


class Location:
    def __init__(self):
        self.latitude = None
        self.longitude = None

    def setlocation(self, locationname):  # Method calls geocode API to return a json object, sometimes cloudflare will
        # trigger causing an error 403, might take a few tries.

        geocodeapi = f"https://geocode.xyz/{locationname}?json=1"
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}
        # Tried to spoof browser to avoid error 403 with headers as above to no tangible benefit

        response = requests.get(geocodeapi)  # Blocking request, will wait for response
        responseObj = response.json()

        if "error" in responseObj:  # catch errors when the API report status = 200
            self.testerrorin200(responseObj)

        elif response.status_code < 300:
            self.setlongitude(responseObj['longt'])
            self.setlatitude(responseObj['latt'])

        else:
            print(f"Failed API call: {response.status_code} \nTry again")

        return response.status_code

    def testerrorin200(self, responseObj):
        if responseObj['error']['code'] == '006':
            raise Exception(f"Error {responseObj['error']['code']}: API Request Throttled, please wait some time "
                            f"and try again")  # API throttling issue

        elif responseObj['error']['code'] == '018':
            raise Exception(
                f"Error {responseObj['error']['code']}: Location not found")  # Exception raised if location is invalid

        else:
            raise Exception("Error, please try again")  # Generic exception as a precaution

    def getforecast(self):
        openmeteoapi = f'https://api.open-meteo.com/v1/forecast?latitude={self.getlatitude()}&longitude={self.longitude}&hourly=temperature_2m'

        response = requests.get(openmeteoapi)
        if response.status_code > 200:
            print(f"Failed API call: {response.status_code} \nTry again")
            self.getforecast()  # calls method recursively till a non error response is received
        obj = response.json()
        return obj['hourly']  # returns only the hourly data

    def getlongitude(self):
        return self.longitude

    def getlatitude(self):
        return self.latitude

    def setlongitude(self, longitude):
        self.longitude = longitude

    def setlatitude(self, latitude):
        self.latitude = latitude
