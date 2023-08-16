import requests

# Define the API endpoint with the provided IPv4 address
url = "http://139.59.91.37:5000/api/messages"

# Define the message data
data = {
    "message": "Hello, Server!"
}

# Send a POST request to the server
response = requests.post(url, json=data)

# Print the server's response
print(response.text)
