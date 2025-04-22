import pandas as pd
import janitor
import random as r
from pymongo import MongoClient

#connect to database
conn_str = 'connection_string_goes_here'
client = MongoClient(conn_str)

#read in csv
df = pd.read_csv('data/Air_Quality_Continuous.csv')

try:
    #filter to station 452
    df = df[df['Site_ID'] == 452.0]

    #clean columns
    df = (
        #rename objectid2 and site_id
        df.rename(columns={'ObjectId2':'_id','Site_ID':'station_id'})
        #make PK and FK first two columns
        .reorder_columns(['_id','station_id'])
        #rename columns
        .clean_names()
    )

    #remove rows with missing foreign key
    df = df[df['station_id'].notna()]

    #change site id to integer
    df['station_id'] = df['station_id'].astype(int)

    #remove outliers
    df = df[df['date_time'].str[:4] != '2611']

    #clean date_time
    df['date_time'] = pd.to_datetime(df['date_time']).dt.strftime('%Y-%m-%d %H:%M')

    #make sure nulls can be handled by mongodb
    df = df.where(pd.notnull(df), None)

except Exception as e:
    print(f"There was an error: {e}")

try:
    #randomly select sample of rows
    sample_size = 10000
    selection = r.sample(range(len(df)), sample_size)
    df = df.iloc[selection, :]

    #check date range of sample
    first_date = df['date_time'].min()
    last_date = df['date_time'].max()

    print(f"The data now ranges from {first_date} to {last_date}.")
    
except Exception as e:
    print(f"There was an error: {e}")

#write to csv
try:
    df.to_csv('nosql_data.csv', index=False, encoding='utf-8')

    print("Data exported successfully!")

except Exception as e:
    print(f"There was an error: {e}")