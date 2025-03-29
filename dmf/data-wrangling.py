import numpy as np
import pandas as pd
import pyjanitor

#read in csv
df = pd.read_csv('./Air_Quality_Continuous.csv')

#sort by timestamp
df = df.sort_values(by=['Date_Time'], ascending=True)

#check for empty variables
print(df.isnull().all())

#check if objectid2 is unique
print(df['ObjectId2'].is_unique)

#clean columns
df = (
    #remove objectid
    df.drop('ObjectId', axis=1)
    #make objectid into primary key
    .rename(columns={'ObjectId2':'id'})
    #reorder columns
    .reorder_columns(['id'])
    #rename columns
    .clean_names()
    .rename(columns=lambda col: f"r_{col}")
)

#check for missing rows
num_rows = df.shape[0]
if num_rows == 1603492:
    print("No rows missing")

#check dataframe
df.head()