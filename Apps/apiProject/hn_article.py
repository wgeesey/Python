import requests   # Requests library
import json   # JSON module


# Make an API call, and store the response.
# url variable to hold the API endpoint desired.
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"

# Use request library to make GET request.
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
# Parse the JSON content to a Python dictionary.
response_dict = r.json()

# Convert the dictionary to JSON string. Indentation for readability.
response_string = json.dumps(response_dict, indent=4)
print(response_string)