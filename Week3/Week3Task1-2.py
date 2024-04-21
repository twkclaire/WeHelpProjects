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
mrtlist = []
for item in list2:
    mrt = item["MRT"].split('／')[0]
    districts = item["address"].split(' ')[2][:3]
    existing_mrts = [list(d.keys())[0] for d in mrtlist]
    if mrt not in existing_mrts:
        mrtlist.append({mrt: districts})

direction_list = []
for item in list1:
    directions = item["info"]
    spots = item["stitle"]
    direction_list.append({spots: directions})
  
attraction_mrt_list = []
for attraction in direction_list:
    attraction_name = list(attraction.keys())[0]
    attraction_info = list(attraction.values())[0]
    mrt_found=False #reset after each loop

    for mrt_station in mrtlist:
        station_name = list(mrt_station.keys())[0]
        station_district = list(mrt_station.values())[0]

        if station_name in attraction_info:
            beitou="北投"
            if station_name != "北投":
                attraction_mrt_list.append({"Attraction": attraction_name, "MRT": station_name, "District": station_district})
                mrt_found=True
                break  # Stop searching for MRT stations once one is found for the attraction
            else: 
                attraction_mrt_list.append({"Attraction": attraction_name, "MRT": "新北投", "District": "北投區"})
                mrt_found=True
                break
    if not mrt_found:
    # Append a dictionary with empty strings if no matching MRT station is found
       attraction_mrt_list.append({"Attraction": attraction_name, "MRT": "", "District": ""})

# print(len(attraction_mrt_list))

new_list=[]
for item in attraction_mrt_list:
    if item["Attraction"] =="北投文物館":
        item["MRT"]= "北投"
        new_list=attraction_mrt_list

# for dict in new_list:
    # print(dict)


attraction_groups = {}

for attraction in new_list:
    mrt_station = attraction["MRT"]
    if mrt_station not in attraction_groups:
        attraction_groups[mrt_station] = [attraction["Attraction"]]
    else:
        attraction_groups[mrt_station].append(attraction["Attraction"])

for mrt_station, attractions in attraction_groups.items():
    if len(mrt_station) !=0:
        print(f"{mrt_station}: {', '.join(attractions)}")
    
import csv

csv_filename = "mrt.csv"

with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:

    csv_writer = csv.writer(csv_file)
    # Write each attraction group to the CSV file
    for mrt_station, attractions in attraction_groups.items():
        if len(mrt_station) !=0:
            csv_writer.writerow([f"{mrt_station}: {', '.join(attractions)}"])

