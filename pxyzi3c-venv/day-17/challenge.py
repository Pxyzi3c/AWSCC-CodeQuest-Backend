import pip._vendor.requests as requests

base_url = "https://jsonplaceholder.typicode.com/"
entity = {
    "users": None
}

response = requests.get(f"{base_url}/users")
if response.status_code == 200:
    print("Request successful.")
    entity['users'] = response.json()
else:
    print("Request failed.")

for user in entity["users"]:
    print(user['name'])