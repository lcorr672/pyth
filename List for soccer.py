import random 

name = input('Player Name: ') 
number = input('Player Number: ') 

team = ['kevin 42', 'Kayle 8', 'kyle 12', 'dog 67', 'person 4', 'leyla 8', 'Diana 8']
teammates = random.choices(team, k=5)
#got lost needed help to remove square brackets REMBER THIS COMMAND 
teammates_str = ", ".join(teammates)

text = f'Welcome to the team, {name}! Your team number is {number}. Here are your teammates: {teammates_str}'

print(text)
