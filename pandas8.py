#read csv file in excel sheet
import pandas as pd

df = pd.read_csv('sample_data.csv')
print(df.to_string(index=False))
