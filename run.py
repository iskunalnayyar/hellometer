import datetime
import os
import sqlite3
import math
import pandas as pd

from flask import Flask, render_template, Response

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "interview-app.db")

'''
0 => Dec 31 1969 7:00PM GMT
1979615 => Jan 23rd 1970 4:53PM GMT
'''

@app.route('/')
def list_of_doctors():
    data = pd.read_csv('WithTime.csv')
    dates = pd.to_datetime(data['first_seen_datetime_utc']).dt.day.tolist()
    # print(dates)
    hours = pd.to_datetime(data['first_seen_datetime_utc']).dt.hour.tolist()
    # print(hours)
    # print(len(hours))
    users_per_hour = []
    distinct_hrs = []
    data = data.set_index(pd.to_datetime(data['first_seen_datetime_utc']))
    mean_tts_ls = data.resample('H').mean()['tts'].tolist()
    mean_tts = [0 if math.isnan(x) else x for x in mean_tts_ls]

    count = 1
    left, right = 0, 1
    while right < len(hours):
        cur_avg = []
        while right < len(hours) and hours[left] == hours[right]:
            right += 1
            count += 1
        users_per_hour.append(count)
        distinct_hrs.append(hours[left])
        count = 1
        left = right + 1
        right += 1

    day_part_one = data.loc[data['day_part'] == 1]['tts'].tolist()  # tts
    day_part_one_dates = data.loc[data['day_part'] == 1]['first_seen_utc'].tolist()  # dates
    day_part_two = data.loc[data['day_part'] == 2]['tts'].tolist()
    day_part_three = data.loc[data['day_part'] == 3]['tts'].tolist()
    day_part_four = data.loc[data['day_part'] == 4]['tts'].tolist()
    day_part_five = data.loc[data['day_part'] == 5]['tts'].tolist()
    day_part_six = data.loc[data['day_part'] == 6]['tts'].tolist()
    tts = data['tts'].tolist()
    arr = [i for i in range(len(tts))]

    context = {
        'tts': tts,
        'tts_counter': arr,
        'mean_tts': mean_tts,
        'dist_hrs': distinct_hrs,
        'cust_per_hour': users_per_hour,
        'day_part_one': day_part_one,
        'day_part_one_dates': day_part_one_dates,
        'day_part_two': day_part_two,
        'day_part_three': day_part_three,
        'day_part_four': day_part_four,
        'day_part_five': day_part_five,
        'day_part_six': day_part_six
    }

    # day_part_one = is_one['tts']
    # print(day_part_one)
    return render_template('first_view.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
