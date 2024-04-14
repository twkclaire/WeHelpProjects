import math 

def get_number(index):
    n= index+1
    nth = (n-1)*4 - (math.floor((n-1)*1/3))*5
    print(nth)

get_number(1) # print 4
get_number(5) # print 15 
get_number(10) # print 25 
get_number(30) # print 70