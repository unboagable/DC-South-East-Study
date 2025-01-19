import geopandas as gpd
import pandas as pd

# Load TIGER/Line shapefile
shapefile_path = "data/raw/shapefiles/tl_2024_11_tract/tl_2024_11_tract.shp"
tracts_gdf = gpd.read_file(shapefile_path)

# Load your dataset (assuming it's in a CSV)
data_path = "data/processed/track/DC-filtered_EJScreen_2024_Tract_StatePct_with_AS_CNMI_GU_VI.csv"
data_df = pd.read_csv(data_path)

# Convert GEOID to string for joining
data_df['ID'] = data_df['ID'].astype(str).str.split('.').str[0]  # Remove ".0"
tracts_gdf['GEOID'] = tracts_gdf['GEOID'].astype(str)

# Merge the shapefile and your data
merged_gdf = tracts_gdf.merge(data_df, left_on='GEOID', right_on='ID', how='left')

#
merged_gdf.to_file("data/processed/shapefiles/track/merged_shapefile.shp")


# Plot merged data
#merged_gdf.plot(column='LOWINCPCT', cmap='OrRd', legend=True)

