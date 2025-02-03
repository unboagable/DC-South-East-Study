import requests
import json
import pandas as pd
import time

# Define the API endpoint
url = "https://ejscreen.epa.gov/mapper/ejscreenRESTbroker1.aspx"

# List of block group IDs for southeast of Anacostia
block_groups_anacostia = [
    "110010074011", "110010074012", "110010074021", "110010074022",
    "110010075011", "110010075012", "110010075021", "110010075022",
    "110010076011", "110010076012", "110010076021", "110010076022",
    "110010077011", "110010077012", "110010077021", "110010077022",
    "110010078011", "110010078012", "110010078021", "110010078022",
    "110010079011", "110010079012", "110010079021", "110010079022",
    "110010080011", "110010080012", "110010080021", "110010080022",
    "110010081011", "110010081012", "110010081021", "110010081022",
    "110010082011", "110010082012", "110010082021", "110010082022"
]

def get_ejscreen_data(params, area_id=None):
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant fields
        demographics = data.get("data", {}).get("demographics", {})
        main_stats = data.get("data", {}).get("main", {})
        extras = data.get("extras", {})

        # Flatten the data
        flattened_data = {
            "area_id": area_id,  # Add area_id for tracking
            "total_population": demographics.get("TOTALPOP"),
            "percent_minority": demographics.get("PCT_MINORITY"),
            "per_capita_income": demographics.get("PER_CAP_INC"),
            "unemployment_rate": demographics.get("P_EMP_STAT_UNEMPLOYED"),
            "pm25_air_quality": main_stats.get("RAW_E_PM25"),
            "traffic_exposure": main_stats.get("RAW_E_TRAFFIC"),
            "diesel_particulate_matter": main_stats.get("RAW_E_DIESEL"),
            "life_expectancy": extras.get("RAW_HI_LIFEEXP", "N/A")
        }
        
        return flattened_data
    else:
        print(f"Error fetching data for {area_id}: {response.status_code}")
        return None

def get_ejscreen_data_city(city, area_id):
    params = {
        "namestr": city,
        "geometry": "",
        "distance": "",
        "unit": "9035",
        "areatype": "city",
        "areaid": area_id,
        "f": "json"
    }
    return get_ejscreen_data(params, area_id=area_id)
        
def get_ejscreen_data_bg(area_id):
    params = {
        "namestr": area_id,
        "geometry": "",
        "distance": "",
        "unit": "9035",
        "areatype": "blockgroup",
        "areaid": area_id,
        "f": "json"
    }
    return get_ejscreen_data(params, area_id=area_id)

# Get data for all block groups southeast of Anacostia
data_anacostia = []
for bg in block_groups_anacostia:
    result = get_ejscreen_data_bg(bg)  # Fixed function call
    if result:
        data_anacostia.append(result)
    time.sleep(1)  # Avoid overwhelming the API

# Convert to DataFrame
df_anacostia = pd.DataFrame(data_anacostia)

# Fetch data for DC
data_dc = get_ejscreen_data_city("Washington", "1150000")

# Convert to DataFrame (fix potential issue with dictionary)
df_dc = pd.DataFrame([data_dc])

# Display data
print("EJScreen Data - Southeast Anacostia:")
print(df_anacostia.head())

print("\nEJScreen Data - Washington, DC:")
print(df_dc.head())
