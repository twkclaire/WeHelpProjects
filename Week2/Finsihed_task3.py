def func(*data):
    name_dict = {}
    for name in data:
        if len(name)==2 or len(name)==3:
            dic = {name[1]:name} #create dictionary for middle name and full name
            if name[1] not in name_dict: #check middle name in dictionary if doesn't exist, add it to the list
                name_dict.update(dic) 
            else:
                name_dict.pop(name[1]) #if it exists already, remove the duplicated name from the list
        elif len(name)==4 or len(name)==5:
            dic = {name[2]:name}
            if name[2] not in name_dict:
                name_dict.update(dic)
            else:
                name_dict.pop(name[2])

    if name_dict== {}: #if dictionary is empty than print nothing special
        print("沒有誒")
    else:    
        for values in name_dict.values(): #if not, print the value which is the full name
            print(values)

func("彭大牆", "陳王明雅", "吳明") 
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有 
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安