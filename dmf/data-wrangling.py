import numpy as np
import pandas as pd

#read in csv
df = pd.read_csv('./Air_Quality_Continuous.csv')

#sort by timestamp
df = df.sort_values(by=['Date_Time'], ascending=True)

#display first 5 rows
df.head()

#check for empty variables
print(df.isnull().all())

#check if objectid2 is unique
print(df['ObjectId2'].is_unique)

#remove objectid
df = df.drop('ObjectId', axis=1)

#check for missing rows
num_rows = df.shape[0]
if num_rows == 1603492:
    print("No rows missing")