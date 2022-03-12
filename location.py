import requests


class Location:
    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.location = None
        self.forecastdict = None

    def setlocation(self, response):
        if "error" in response:  # catch errors when the API returns successfully
            self.testerrorin200(response)

        self.latitude = response['latt']
        self.longitude = response['longt']
        self.location = response['standard']['city']

        print(str(self.location) + " is located at: " + str(self.latitude) + " " + str(self.longitude))

    def geocodeapi(self, locationname):
        api = f"https://geocode.xyz/{locationname}?json=1"
        response = requests.get(api)

        return self.setlocation(self.testerror(response))

    def testerror(self, response):
        if response.status_code <= 204:
            print(f"{response.status_code}: API Response successful.")
            return response.json()

        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: Cloudflare triggered, please try again.")

        else:
            raise Exception(f"Error {response.status_code}: API did not return correctly, please try again.")

    def testerrorin200(self, responseObj):
        if responseObj['error']['code'] == '006':
            raise Exception(f"Error {responseObj['error']['code']}: API Request Throttled, please wait some time."
                            f"and try again")  # API throttling issue

        elif responseObj['error']['code'] == '018':
            raise Exception(
                f"Error {responseObj['error']['code']}: Location not found.")  # Exception raised if location is invalid

        else:
            raise Exception(
                f"Error {responseObj['error']['code']}: Please try again.")  # Generic exception as a precaution

    def forecastapi(self):
        openmeteoapi = f'https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&hourly=temperature_2m'
        response = requests.get(openmeteoapi)

        return self.getforecast(self.testerror(response))

    def getforecast(self, response):
        if "error" in response:  # catch errors when the API returns successfully
            self.testerrorin200(response)

        return response['hourly']

    def getweather(self, fcast):
        my_dict = {}

        for x, y in zip(fcast['time'], fcast['temperature_2m']):  # for loop printing time/temperature
            datetime = str(x).replace("T", " Time: ")
            temp = str(y) + "°C"
            entry = {datetime: temp}
            my_dict.update(entry)
        self.forecastdict = my_dict


def printdict(my_dict):
    for key, value in my_dict.items():
        print(key, value)
