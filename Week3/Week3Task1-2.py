import urllib.request as request
import ssl
import json

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE

src1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

# Load data from the first URL
with request.urlopen(src1, context=context) as response:
    data1 = json.load(response)
    list1 = data1["data"]["results"]

# Load data from the second URL
with request.urlopen(src2, context=context) as response:
    data2 = json.load(response)
    list2 = data2["data"]

#created list of dictionary for {attractiont} {mrt} {district} ======================================


mrt_list = []

for item in list2:
    mrt = item["MRT"]
    mnumber=item["SERIAL_NO"]
    mrt_list.append({mnumber:mrt})
# print(mrt_list)

title_list = []
for item in list1:
    title = item["stitle"]
    number = item["SERIAL_NO"]
    title_list.append({number: title})
# print(title_list)
  
mrt_title_list=[]      

mrt_title_list = []
for mrt_dict in mrt_list:
    for title_dict in title_list:
        mnumber = list(mrt_dict.keys())[0]
        number = list(title_dict.keys())[0]
        if mnumber == number:
            mrt = list(mrt_dict.values())[0]
            title = list(title_dict.values())[0]
            mrt_title_list.append({mrt: title})

# print(mrt_title_list)
# print(len(mrt_title_list))

mrt_spots_dict = {}

for item in mrt_title_list:
    key = list(item.keys())[0]
    value = list(item.values())[0]

    if key not in mrt_spots_dict:
        mrt_spots_dict[key] = [value]
    else:
        mrt_spots_dict[key].append(value)
    
print(mrt_spots_dict)

import csv
csv_filename = "mrtlast.csv"

# Determine the maximum number of attractions across all stations
max_attractions = max(len(attractions) for attractions in mrt_spots_dict.values())

with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write each attraction group to the CSV file
    for mrt_station, attractions in mrt_spots_dict.items():
        if len(mrt_station) != 0:
            # Initialize a row with the MRT station
            row = [mrt_station]

            # Add attractions to the row, ensuring each attraction is in a separate column
            for i in range(max_attractions):
                if i < len(attractions):
                    row.append(attractions[i])
                else:
                    row.append("")  # Add empty string if there are no more attractions

            # Write the row to the CSV file
            csv_writer.writerow(row)


