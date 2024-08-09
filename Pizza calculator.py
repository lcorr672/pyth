number_of_people_left_to_feed = int(input('people')) 

number_largepizza = number_of_people_left_to_feed // 7 #ans without ans
left = number_of_people_left_to_feed % 7 #remainder


number_mediumpizza = left // 3 
number_mediumpizza2 = left % 3 

number_small = number_mediumpizza2 // 1 

text = f'large {number_largepizza}, Meduim {number_mediumpizza}, small pizza {number_small}' 
print(text) 
