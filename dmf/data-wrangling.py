import numpy as np
import pandas as pd

# read in csv
df = pd.read_csv('./Air_Quality_Continuous.csv')

# sort by VPM10
df.sort_values(by=['VPM10'])

# display first 5 rows
df.head()

# check if ObjectId2 is unique and can be used as a primary key
df['ObjectId2'].is_unique