import pip._vendor.requests as request

base_url = "https://api.spacexdata.com/v5"

class SpaceXLaunchesClass:
    def __init__(self):
        self.latest = None

    @property
    def apiUrl(self):
        return f"{base_url}/launches"
    
    def getLatest(self):
        headers = {
            "User-Agent": "MyApp/1.0"     
        }

        params = {
            "_format": "json"
        }

        response = request.get(f"{self.apiUrl}/latest", headers=headers, params=params)
        self.handleResponse(response)

    def handleResponse(self, response):
        if response.status_code == 200:
            print(f"Status code: {response.status_code}")
            self.displayHeaders(response.headers)
            self.latest = self.setLatest(response.json())
        else:
            print(f"Process failed with status: {response.status_code}")

    def displayHeaders(self, headers: object):
        print("Response Headers:")
        for key, value in headers.items():
            print(f"{key}: {value}")
    
    def setLatest(self, launch: object):
        return {
            "id": launch['id'],
            "name": launch['name'],
            "flight_number": launch['flight_number'],
            "details": launch['details'],
            "crew": launch['crew'],
            "ships": launch['ships'],
        }

def start():
    space_x_launches = SpaceXLaunchesClass()
    space_x_launches.getLatest()

start()