import requests

# Example GET request to fetch user data
response = requests.get("https://api.example.com/users/123")
if response.status_code == 200:
    print("GET Response:", response.text)

# Example POST request to create a new user
new_user_data = {"username": "new_user", "email": "new@example.com"}
response = requests.post("https://api.example.com/users", json=new_user_data)
print("POST Response:", response.text)

# Example PUT request to update user information
updated_data = {"email": "updated@example.com"}
response = requests.put("https://api.example.com/users/123", json=updated_data)
print("PUT Response:", response.text)

# Example DELETE request to remove a user
response = requests.delete("https://api.example.com/users/123")
print("DELETE Response:", response.text)

# API ENDPOINTS
# Base URL
base_url = "https://api.example.com/v1"

# Resource Path
resource_path = "/users"

# Parameters
parameters = {"status": "active", "sort": "desc"}

# Construct the complete endpoint URL
endpoint_url = base_url + resource_path

# Adding parameters to the URL
if parameters:
    endpoint_url += "?" + "&".join([f"{key}={value}" for key, value in parameters.items()])

# Sending a GET request to the constructed endpoint URL
response = requests.get(endpoint_url)

# Handle the response as needed
print("API Response:", response.text)