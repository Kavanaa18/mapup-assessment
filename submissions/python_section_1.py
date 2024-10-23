## Question 1: Reverse List by N Elements

def reverse_by_n(list1,n):
    for i in range(0,len(list1),n):
        start = i
        end =min(i+n-1 , len(list1)-1)

        while start<end:
            list1[start],list1[end] =list1[end],list1[start]
            start +=1
            end -=1
        
        return list1
    
# list1 = [1,2,3,4,5,6,7]
# n =3
# print(reverse_by_n(list1,n))

## Question 2: Lists & Dictionaries



def list_to_dict_group(string1):
    dict1={}

    for i in string1:
        str_len =len(i)

        if str_len not in dict1:
            dict1[str_len]=[]

        dict1[str_len].append(i)

    sort_dict1 = dict(sorted(dict1.items()))
    return sort_dict1

# string1 =["apple" ,"a" ,"ball" , "cat"] 
# print(list_to_dict_group(string1))



## Question 3: Flatten a Nested Dictionary

def flatten_dict(nested_dict, parent_key='', sep='.'):
    items = {}

    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        
        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, sep=sep))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    items.update(flatten_dict(item, f"{new_key}[{i}]", sep=sep))
                else:
                    items[f"{new_key}[{i}]"] = item
        else:
            items[new_key] = value

    return items

# nested_dict = {
#     "road": {
#         "name": "Highway 1",
#         "length": 350,
#         "sections": [
#             {
#                 "id": 1,
#                 "condition": {
#                     "pavement": "good",
#                     "traffic": "moderate"
#                 }
#             }
#         ]
#     }
# }

# flattened_dict = flatten_dict(nested_dict)
# print(flattened_dict)

## Question 4: Generate Unique Permutations

from itertools import permutations

def generate_unique_permutation(list2):
    unique_perm = set(permutations(list2))

    return [list(i) for i in unique_perm]

# ls = [1,1,2]
# print(generate_unique_permutation(ls))


## Question 5: Find All Dates in a Text

import re

def find_all_dates(text):
    patterns = [
        r'\b(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})\b',
        r'\b(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})\b',
        r'\b(\d{4})\.(0[1-9]|1[0-2])\.(0[1-9]|[12][0-9]|3[01])\b'
    ]

    valid_date =[]

    for pattern in patterns:
        matches = re.findall(pattern,text)

        for i in matches:
            if pattern == r'\b(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})\b':
                valid_date.append(f"{i[0]}-{i[1]}-{i[2]}")
            elif pattern == r'\b(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})\b':
                valid_date.append(f"{i[0]}/{i[1]}/{i[2]}")
            else:
                valid_date.append(f"{i[0]}.{i[1]}.{i[2]}")
    return valid_date
    
# text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23. Invalid date 18-15-2022."
# print(find_all_dates(text))

## Question 6: Decode Polyline, Convert to DataFrame with Distances

import polyline
import pandas as pd
from haversine import haversine

def decode_polyline(code):
    coordinates = polyline.decode(code)


    df = pd.DataFrame(coordinates,columns=['latitude','longitude'])

    distance =[0.0]

    for i in range(1,len(coordinates)):
        prev_point = (coordinates[i-1][0], coordinates[i-1][1])
        curr_point = (coordinates[i][0],coordinates[i][1])
        dist = haversine(prev_point,curr_point)
        distance.append(dist)

    df['distance'] = distance

    return df

# poly_str = "ezdvBcps}Lt@W@F@BVKl@UK]Wc@}@kAOKBEzA{BdA}Ab@s@LBf@RjARZBv@?rAAfBIX?f@FLBf@^b@hATbAF~@BvB?hALjBHpCLjAVdAd@dAxCbGlA~BbBvCpAbD`AnCVpB\\hBf@nB|@tAb@f@RVXLbDj@jCl@nAf@`DbBdC`B`@b@HNN`@lA~DnAvBvB`G\\fA^p@j@z@~E`FbBpBxDfFXh@|@pD`@bB^fANd@\\`Bl@rBb@fATj@v@bBjBwCd@w@NB^B\\@\\K\\Q|AWZGXOPIRBb@K\\Kl@_@VOZWVI^Eh@Ov@KxCJ\\@\\K^@RMh@QhAMXKXY`@Q^SLK`@]fBc@n@M\\OlB_@n@KNMRUZQZGh@Ht@Lx@F`@BTANDRNTPNDDHLXN`@LRTJx@?RBJFFLV\\Zs@TQ`@MVIhAYp@YPc@VgALk@Hk@d@eA\\cAHq@Eo@J}@@q@DItAgAv@i@|@e@v@k@bAaAdDuB|@c@?I?]?{@Ms@COFWJODYEcABOTU^e@H_@Km@Ci@BU?e@Ca@Ie@e@oBKk@Eu@M{@CoAC}@Km@Iy@IaA?{@Ci@Ms@UgA]y@Mm@GQICe@QKMGi@Gi@GSI[Ym@[{@@_AK]SMo@i@OCg@EOEMMYSi@IUO]Ko@KSIWUWMU_@I]Kw@WoACY@a@CWQWe@[QIOYMYW]SMQUQu@OWWSUWU[SsAEg@Ic@Mc@?a@Ai@Em@AUOa@M_@e@g@MSGYOY_@YIQSR[Pa@mBQaAI[@QDyACq@Iu@o@k@e@Y]IcAAmBC]Ee@IgAUWAw@Ae@GWSaAeAYk@Si@a@k@YAc@O{@]a@MnAqA~@mCVaAHk@YmCIQSQOS"
# print(decode_polyline(poly_str))


## Question 7: Matrix Rotation and Transformation

def matrix_rotation_transform(matrix):
    n = len(matrix)

    rotate_matrix = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            rotate_matrix[j][n-1-i] = matrix[i][j]


    final_matrix = [[0]*n for j in range(n)]

    for i in range(n):
        for j in range(n):
            row_sum = sum(rotate_matrix[i])
            col_sum = sum(rotate_matrix[k][j] for k in range(n))
            
            final_matrix[i][j] = row_sum+col_sum - (2*rotate_matrix[i][j])

    return final_matrix

# matrix = [[4,5,3],[6,9,2],[1,3,2]]
# print(matrix_rotation_transform(matrix))


## Question 8: Time Check

import pandas as pd

def time_check(df):
    df["startTime"] = pd.to_datetime(df["startTime"],format ="%H:%M:%S").dt.time #convert dtype to datetime
    df["endTime"] =pd.to_datetime(df["endTime"],format="%H:%M:%S").dt.time

    grouped = df.groupby(["id" ,"id_2"])

    def time_coverage(group):
        start_time = group['startTime'].min()==pd.to_datetime("00:00:00",format="%H:%M:%S").time()
        end_time = group["endTime"].max()==pd.to_datetime("23:59:59",format="%H:%M:%S").time()
        days = set(group["startDay"]).union(group["endDay"]) == set(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])

        return start_time and end_time and days
    
    results = grouped.apply(time_coverage)

    return results

# df = pd.read_csv(r"C:\projects\MapUp-DA-Assessment-2024\datasets\dataset-1.csv")
# print(time_check(df))
