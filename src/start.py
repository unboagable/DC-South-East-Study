import pandas as pd

FILENAME = 'data/EJSCREEN_2024_BG_StatePct_with_AS_CNMI_GU_VI.csv'
df = pd.read_csv(FILENAME, index_col=0, encoding='utf-8')
print(df.head(5))

# Step 3: Programmatically Identify Relevant Columns
def identify_columns(df):
    print("Available columns:")
    for col in df.columns:
        print(col)

if df is not None:
    identify_columns(df)
