import pandas as pd

FILENAME = 'data/EJSCREEN_2024_BG_StatePct_with_AS_CNMI_GU_VI.csv'
data = pd.read_csv(FILENAME, index_col=0, encoding='utf-8')

# Programmatically Identify Relevant Columns
def identify_columns(data):
    print("Available columns:")
    for col in data.columns:
        print(col)

if data is not None:
    identify_columns(data)

# Filter for Washington, DC and then for Anacostia
def filter_anacostia(data, keyword="Anacostia"):
    # Step 1: Filter for DC
    dc_data = data[data['ST_ABBREV'] == 'DC']
    print(f"Filtered data for Washington, DC: {dc_data.shape[0]} rows")

# Filter for Anacostia
if data is not None:
    anacostia_data = filter_anacostia(data, 'Anacostia')
