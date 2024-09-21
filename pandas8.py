#read csv file in excel sheet
import pandas as pd
data = {
    'ID': [1, 2, 3, 4],
    'Name': ['ebi', 'blessy', 'angel', 'ebin'],
    'Age': [21, 22, 23, 24],
    'City': ['uthumalai', 'surandai', 'tenkasi', 'tirunelveli']
}


df = pd.DataFrame(data)
csv_file_path ='Desktop/sample_data.csv'
df.to_csv(csv_file_path, index=False)

csv_file_path
