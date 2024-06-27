import pandas as pd

file = 'data/EJSCREEN_2023_BG_StatePct_with_AS_CNMI_GU_VI.csv'
df = pd.read_csv(file, index_col=0)
print(df.head(5))