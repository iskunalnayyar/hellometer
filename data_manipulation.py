import pandas as pd
from time import time, ctime

data = pd.read_csv('data_aug27.csv')
print(data.columns)

data = data.sort_values(by=['first_seen_utc'])
print(data['first_seen_utc'])

data['first_seen_datetime_utc'] = pd.to_datetime(data['first_seen_utc'], unit='s')

# print(data['first_seen_datetime_utc'].tolist())
times = pd.to_datetime(data['first_seen_datetime_utc']).dt
print(times.hour.tolist())

# data.to_csv('WithTime.csv', index=False)