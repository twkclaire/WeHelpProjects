station_positions = {
        "Songshan": 0,
        "Nanjing Sanmin": 1,
        "Taipei Arena": 2,
        "Nanjing Fuxing": 3,
        "Songjiang Nanjing": 4,
        "Zhongshan": 5,
        "Beimen": 6,
        "Ximen": 7,
        "Xiaonanmen": 8,
        "Chiang Kai-shek Memorial Hall": 9,
        "Guting": 10,
        "Taipower Building": 11,
        "Gongguan": 12,
        "Wanlong": 13,
        "Jingmei": 14,
        "Dapinglin": 15,
        "Qizhang": 100,
        "Xiaobitan": 100,
        "Xindian City Hall":17,
        "Xindian": 18,   
    }


messages={
    "Leslie":"I'm at home near Xiaobitan station.", 
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.", 
    "Copper":"I just saw a concert at Taipei Arena.", 
    "Vivian":"I'm at Xindian station waiting for you."
}

def find_and_print(messages, current_station):
    def get_current_station(current_station):
        for my_station, my_position in station_positions.items():
            if my_station == current_station:
                return my_position


    def get_station(message):
        for station, position in station_positions.items():
            if station in message:
                return station, position
    current_position = get_current_station(current_station)        

    update_list=[]
    for name, message in messages.items():
        station,position = get_station(message)
        update_list.extend([[name, station, position]])
# print(update_list)    

    our_distance= 0
    closest_friend=0
    closest_distnace=100

    for people, location, far in update_list:
        our_distance = abs(current_position - far)
        # print(our_distance)
        if our_distance < closest_distnace:
            closest_distnace= our_distance
            closest_friend = people
    print(closest_friend) 


find_and_print(messages, "Wanlong") # print Mary 
find_and_print(messages, "Songshan") # print Copper 
find_and_print(messages, "Qizhang") # print Leslie 
find_and_print(messages, "Ximen") # print Bob 
find_and_print(messages, "Xindian City Hall") # print Vivian