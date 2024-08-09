number_of_people_left_to_feed = int(input('people')) #Does not recognize number str, Twenty will not work but, 20 will 

number_largepizza = number_of_people_left_to_feed // 7 #ans without remainder the actual number of Large pizzas 
left = number_of_people_left_to_feed % 7 #remainder taken, then put down the line 


number_mediumpizza = left // 3 #taken remainder to get meuim number of pizzas 
number_mediumpizza2 = left % 3 #remainder again 

number_small = number_mediumpizza2 // 1 # final number 

text = f'large {number_largepizza}, Meduim {number_mediumpizza}, small pizza {number_small}' 
print(text) 
