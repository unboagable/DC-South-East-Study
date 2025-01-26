import requests
import json
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

if response.status_code == 200:
    data = response.json()  # Parse JSON response

    # Extract specific fields
    demographics = data.get("data", {}).get("demographics", {})
    main_stats = data.get("data", {}).get("main", {})
    extras = data.get("extras", {})

    # Example: Print a subset of demographics
    print("Demographics:")
    print(f"  Total Population: {demographics.get('TOTALPOP')}")
    print(f"  Percent Minority: {demographics.get('PCT_MINORITY')}%")
    print(f"  Per Capita Income: ${demographics.get('PER_CAP_INC')}")
    print(f"  Unemployment Rate: {demographics.get('P_EMP_STAT_UNEMPLOYED')}%")

    # Example: Print environmental factors
    print("\nEnvironmental Factors:")
    print(f"  Air Quality (PM2.5): {main_stats.get('RAW_E_PM25')} µg/m³")
    print(f"  Traffic Exposure: {main_stats.get('RAW_E_TRAFFIC')} vehicles/day")
    print(f"  Diesel Particulate Matter: {main_stats.get('RAW_E_DIESEL')} µg/m³")

    # Example: Extract a specific extra field
    life_expectancy = extras.get("RAW_HI_LIFEEXP", "N/A")
    print(f"\nHealth Indicator - Life Expectancy: {life_expectancy} years")

    # Flatten the data into a single dictionary
    flattened_data = {**demographics, **main_stats, **extras}

    # Create a DataFrame from the flattened data
    df = pd.DataFrame([flattened_data])

    # Display the DataFrame
    print("DataFrame:")
    print(df)

    # Optionally save the DataFrame to a CSV file
    # df.to_csv("ejscreen_data.csv", index=False)

    print(df.describe())

else:
    print(f"Error: {response.status_code}")

