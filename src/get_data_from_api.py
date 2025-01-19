import requests
import pandas as pd

# Define the API endpoint and parameters
url = "https://ejscreen.epa.gov/mapper/ejscreenRESTbroker1.aspx"

# Define the area ID as a variable
area_id = "110010088022"

params = {
    "namestr": area_id,
    "geometry": "",
    "distance": "",
    "unit": "9035",
    "areatype": "blockgroup",
    "areaid": area_id,
    "f": "json"
}

# Make the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data)
else:
    print(f"Error: {response.status_code}")


