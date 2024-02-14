import pip._vendor.requests as requests

base_url = "https://jsonplaceholder.typicode.com/users"

def queryStringParameters():
    params = params = {
        "catagory": "electronics",
        "sort": "desc",
        "page": 1,
        "per_page": 2
    }

    response = requests.get(base_url, params=params)

    print(f"Full URL: {response.url}")

    if response.status_code == 200:
        products_data = response.json()
        print(f"Products data: {products_data}")
    else:
        print(f"API request failed with status code: {response.status_code}")

def headers():
    headers = {
        "User-Agent": "MyCustomApp/1.0",
        "Authorization": "Bearer your-access-token"
    }

    response = requests.get(base_url, headers=headers)

    print(f"Response Status Code: {response.status_code}")
    print("Response Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    # Response content (in this case, it's just an example)
    print("Response Content:", response.text)

def requestBodies():
    data = {
        "name": "Harvy Jones Pontillas",
        "email": "harbabes@yahoo.comm"
    }

    post_response = requests.post(base_url, json=data)
    put_response = requests.put(f"{base_url}/2", json=data)

    print(f"POST Response: {post_response.status_code}")
    print(f"PUT Response: {put_response.status_code}")

def start():
    requestBodies()

start()
