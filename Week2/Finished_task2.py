consultants=[
{"name":"John", "rate":4.5, "price":1000}, 
{"name":"Bob", "rate":3, "price":1200}, 
{"name":"Jenny", "rate":3.8, "price":800}
]
for consultant in consultants: 
    consultant.update({"time":[]})
def book(consultants, hour, duration, criteria):

    #defining start, end time of the appointment
    booking_time_start= hour
    booking_hour= duration 
    booking_time_range=[]
    booking_time_mid = 0
    booking_time_end = 0
    available_consultant=[]
    #map out the exact booking hour
    if duration == 1: 
        booking_time_end = hour
        booking_time_range=[hour]
    elif duration ==2: 
        booking_time_end= hour + duration - 1
        booking_time_range=[hour,booking_time_end]
    elif duration ==3:
        booking_time_end= hour + duration - 1
        booking_time_mid= hour +1
        booking_time_range=[hour, booking_time_mid, booking_time_end]

    # check who is available and add them to the avaible_consultant list
    for free_consultants in consultants: 
        if hour not in free_consultants["time"] and booking_time_end not in free_consultants["time"] and booking_time_mid not in free_consultants["time"]:
            available_consultant.append(free_consultants)
            
    # print(available_consultant)
    # # $$$$$$$$$$$$$$$$Fliter through price or rate$$$$$$$$$$$$$$$$$$$$$$$$$$$
    if len(available_consultant)!=0:
        # print("the available consultants are: ", available_consultant)
            # booking_time_range = list(range(hour, hour+ duration)) (when have time try use this)
        if criteria == "rate":
            max_rate=0
            best_rated_consultant =0
            for rated_consultant in available_consultant:
                if rated_consultant["rate"] > max_rate:
                    max_rate = rated_consultant["rate"]
                    best_rated_consultant=rated_consultant 
            if best_rated_consultant:
                consultant_index = consultants.index(best_rated_consultant)
                consultants[consultant_index]["time"].extend(range(booking_time_start, booking_time_end+1))
                print(best_rated_consultant["name"])
        
        if criteria == "price":
            min_price=3000
            cheapest_consultant=0
            for cheap_consultant in available_consultant: 
                if cheap_consultant["price"] < min_price:
                    min_price = cheap_consultant["price"]
                    cheapest_consultant= cheap_consultant 
            if cheapest_consultant:
                consultant_index = consultants.index(cheapest_consultant)
                consultants[consultant_index]["time"].extend(range(booking_time_start, booking_time_end+1))
                print(cheapest_consultant["name"])              
    else:
        print("No Service") # if no consultant is avaible, ignore the above code block and show no one is available



book(consultants, 15, 1, "price") # Jenny 
#print("this is the updated consultant tatble:", consultants)

book(consultants, 11, 2, "price") # Jenny 
#print("this is the updated consultant tatble:", consultants)

book(consultants, 10, 2, "price") # John 
#print("this is the updated consultant tatble:", consultants)

book(consultants, 20, 2, "rate") # John
#print("this is the updated consultant tatble:", consultants)

book(consultants, 11, 1, "rate") # Bob
#print("this is the updated consultant tatble:", consultants)

book(consultants, 11, 2, "rate") # No Service 
#print("this is the updated consultant tatble:", consultants)

book(consultants, 14, 3, "price") # John
#print("this is the updated consultant tatble:", consultants)#

# problem: time is not blocked properly

# # #  #don't remove
# # # #how do i update to  dictionary when I have existing time? 

# # # # consultants[0].update({"time":[12, 13]}) #add the time slot first
# # # # consultants[0]["time"].extend([14]) # assign time and update
# # # # print(consultants[0])