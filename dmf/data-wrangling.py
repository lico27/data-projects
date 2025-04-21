import numpy as np
import pandas as pd
import janitor

#read in csv
df = pd.read_csv('./Air_Quality_Continuous.csv')

#check if objectid2 is unique
print(df['ObjectId2'].is_unique)

#clean columns
df = (
    #rename objectid2
    df.rename(columns={'ObjectId2':'id','Site_ID':'s_id_fk'})
    #make id first column
    .reorder_columns(['id'])
    #rename columns
    .clean_names()
    .rename(columns=lambda col: f"r_{col}" if col != 's_id_fk' else col)
)

#check for missing rows
num_rows = df.shape[0]
if num_rows == 1603492:
    print("No rows missing")

#check number of missing values in foreign key (site ID)
missing_fk = df[df['s_id_fk'][0:].isnull()]
print(len(missing_fk))

#get ids of rows with missing foreign key for future reference
print(list(missing_fk['r_id']))

#remove rows with missing foreign key
df = df[df['s_id_fk'].notna()]

#change site id to integer
df['s_id_fk'] = df['s_id_fk'].astype(int)

#check type of outlier dates to determine how to remove them
print(type(df['r_date_time'][0]))

#remove outliers
df = df[df['r_date_time'].str[:4] != '2611']

#clean date_time
df['r_date_time'] = pd.to_datetime(df['r_date_time'])

#sort by r_date_time to check it's a timestamp - also confirms that data is cleansed to maximum date (i.e. 22/10/2015)
df = df.sort_values(by=['r_date_time'], ascending=False)

#crop data - remove r_date_time values before 01/01/2015 
df = df[df['r_date_time'] > '2015-01-01']

#confirm successful cropping and check how many rows are left
first_date = df['r_date_time'].min()
last_date = df['r_date_time'].max()
new_length = df.shape[0]

print(f"The data is cropped between {first_date} and {last_date}. There are now {new_length} rows.")

#write to csv
df.to_csv('cropped_data.csv')
