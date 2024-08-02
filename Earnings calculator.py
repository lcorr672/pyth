
total = input('How much do you want to save in a year') 
round(int(total), 2)

Month = round(int(total) / 12, 2) #/ by 12 to get a month


Week = round(int(total) / 7, 2) #/ by 7 to get one day 

perday = round(int(total) / 24, 2) #24 days in a month 

savings = f'Monthly need {Month}. Weekly need {Week}. Saving perday {perday}.' 
print(savings) 
