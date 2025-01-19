import pandas as pd

FILENAME = 'data/EJScreen_2024_Tract_StatePct_with_AS_CNMI_GU_VI.csv'
df = pd.read_csv(FILENAME, index_col=0, encoding='utf-8')

# Programmatically Identify Relevant Columns
def identify_columns(data):
    print("Available columns:")
    for col in data.columns:
        print(col)

if df is not None:
    identify_columns(df)

# Filter rows where 'ST_ABBREV' == 'DC'
dc_filtered_df = df[df['ST_ABBREV'] == 'DC']

# Save the filtered data to a new CSV file
output_file_path = 'data/DC-filtered_EJScreen_2024_Tract_StatePct_with_AS_CNMI_GU_VI.csv'  # Output file path
dc_filtered_df.to_csv(output_file_path, index=False)
