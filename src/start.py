import pandas as pd

FILENAME = 'data/DS4EJ_EJScreen_State_BGLevel_NC_Summarized_By_County.csv'

df = pd.read_csv(FILENAME, index_col=0, encoding='utf-8')
print(df.head(5))