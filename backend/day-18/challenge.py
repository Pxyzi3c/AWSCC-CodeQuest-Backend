import pip._vendor.requests as request

base_url = "https://jsonplaceholder.typicode.com"

class PostClass:
    @property
    def apiUrl(self):
        return f"{base_url}/posts"
    
    def store(self):
        title = "Title"
        description = "Sample description"

        data = {
            "title": f"{title[0:3]}{title[4]}",
            "description": description
        }

        response = request.post(self.apiUrl, json=data)
        if response.status_code == 201:
            print(f"Process successful with status: {response.status_code}")
            print(f"Data: {response.text}")
        else:
            print(f"Process failed with status: {response.status_code}")

    def index(self):
        headers = {
            "User-Agent": "MyApp/1.0."
        }

        response = request.get(self.apiUrl, headers=headers)
        
        if response.status_code == 200:
            print(f"Status code: {response.status_code}")
            print(f"Response headers: {response.headers}")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
            print(f"Response content: {response.text}")
        else:
            print(f"API request failed with status code: {response.status_code}")

def start():
    post_class = PostClass()
    post_class.index()
    post_class.store()

start()