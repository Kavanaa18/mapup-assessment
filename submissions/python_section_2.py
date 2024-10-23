##Question 9: Distance Matrix Calculation

import pandas as pd
import numpy as np

df = pd.read_csv(r"datasets\dataset-2.csv")
# print(df.head())

def calculate_distance_matrix(df):
    
    ids = pd.unique(df[["id_start","id_end"]].values.ravel('K'))
    ids.sort()

    distance_matrix = pd.DataFrame(float("inf") , index=ids , columns=ids)

    for id in ids:  #set diagonal values to 0
        distance_matrix.at[id,id] = 0

    for _, row in df.iterrows():
        distance_matrix.at[row["id_start"],row["id_end"]]=row["distance"]
        distance_matrix.at[row["id_end"],row["id_start"]] = row["distance"]

    for k in ids:
        for i in ids:
            for j in ids:
                if distance_matrix.at[i,k]+distance_matrix.at[k,j]<distance_matrix.at[i,j]:
                    distance_matrix.at[i,j] = distance_matrix.at[i,k]+distance_matrix.at[k,j]
    return distance_matrix

distance_matrix = calculate_distance_matrix(df)
# print(distance_matrix)


## Question 10: Unroll Distance Matrix

def unroll_distance_matrix(distance_matrix: pd.DataFrame) ->pd.DataFrame:
    rows = []
    ids = distance_matrix.index

    for id_start in ids:
        for id_end in ids:
            if id_start !=id_end:
                distance = distance_matrix.at[id_start,id_end]
                rows.append({'id_start':id_start ,"id_end":id_end,"distance":distance})

    result = pd.DataFrame(rows)

    return result
unrolled_df = unroll_distance_matrix(distance_matrix)
# print(unrolled_df)
        
## Question 11: Finding IDs within Percentage Threshold

def find_ids_within_ten_percentage_threshold(unrolled_df:pd.DataFrame,reference_value:int)->list:
    reference_distance = df[df["id_start"] == reference_value]

    average_distance = reference_distance['distance'].mean()

    lower_limit = average_distance *0.9
    upper_limit = average_distance *1.1

    ids_within_range = df[(df["id_start"] != reference_value) & (df["distance"] >=lower_limit) & (df["distance"]<= upper_limit)]

    res = sorted(ids_within_range["id_start"].unique().tolist())
    return res

res = find_ids_within_ten_percentage_threshold(unrolled_df , reference_value=1001400)
# print(res)

## Question 12: Calculate Toll Rate

def calculate_toll_rate(unrolled_df:pd.DataFrame)->pd.DataFrame:
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    for vehicle, rate in rate_coefficients.items():
        df[vehicle] = df['distance'] * rate

    return df
toll_rate = calculate_toll_rate(unrolled_df)
# print(toll_rate)

## Question 13: Calculate Time-Based Toll Rates
import pandas as pd
import numpy as np
from datetime import time

def calculate_time_based_toll_rates(toll_rate_df: pd.DataFrame) -> pd.DataFrame:
    weekday_discount = {
        'morning': 0.8, 
        'day': 1.2,    
        'evening': 0.8, 
    }
    
    weekend_discount = 0.7  #saturday and sunday
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    time_based_tolls = []

    time_intervals = [time(hour=h) for h in range(24)]
    
    for _, row in toll_rate_df.iterrows():
        for day in days_of_week:
            for start_time in time_intervals:
                if day in ['Saturday', 'Sunday']:
                    discount = weekend_discount
                else:
                    if start_time < time(10, 0):
                        discount = weekday_discount['morning']
                    elif start_time < time(18, 0):
                        discount = weekday_discount['day']
                    else:
                        discount = weekday_discount['evening']

                time_based_toll = {
                    'id_start': row['id_start'],
                    'id_end': row['id_end'],
                    'distance': row['distance'],
                    'moto': row['moto'] * discount,
                    'car': row['car'] * discount,
                    'rv': row['rv'] * discount,
                    'bus': row['bus'] * discount,
                    'truck': row['truck'] * discount,
                    'start_day': day,
                    'start_time': start_time,
                    'end_day': day,
                    'end_time': (time((start_time.hour + 1) % 24, start_time.minute))  # 1-hour interval
                }
                time_based_tolls.append(time_based_toll)

    
    time_based_toll_df = pd.DataFrame(time_based_tolls)
    
    return time_based_toll_df





resu = calculate_time_based_toll_rates(toll_rate)
print(resu)

resu.to_csv("resu.csv")

