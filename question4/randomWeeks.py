"""
some code that generate 5 random weeks out of year and get the amount of kids
that were reported missing each week and the total percentage of the cases that
the cases during the 5 random weeks account for

written by Paul Cardoos
question 4
"""
#import array from separte file and random to generate random day
import pandas as pd
from monthDay import calendar
from holiday import count_missing_kids_week
import random

#read data from the csv
data = pd.read_csv('../missingKids.csv')

#get the date of all the children that went missing in thier database
data_frame = pd.DataFrame(data, columns=['missingSince'])

#reserve holiday dates
holiday_days = ['Oct 31', 'Nov 1', 'Nov 2', 'Nov 3', 'Nov 4', 'Nov 5', 'Nov 6', 'Dec 25', 'Dec 26', 'Dec 27', 'Dec 28', 'Dec 29', 'Dec 30', 'Dec 31', 'Jan 1', 'Jan 2', 'Jan 3', 'Jan 4', 'Jan 5', 'Jan 6', 'Nov 22', 'Nov 23', 'Nov 24', 'Nov 25', 'Nov 26', 'Nov 27', 'Nov 28', 'Jul 4', 'Jul 5', 'Jul 6', 'Jul 7', 'Jul 8', 'Jul 9', 'Jul 10']

def generate_random_week():
    """
    params: no parameters
    returns an array of length 7 with a set of any 7 consecutive days in the year
    """
    week = []

    #generate a random day by getting a random index in the array
    random_index = random.randint(0, 364)

    while calendar[random_index] in holiday_days:
        print(calendar[random_index])
        random_index = random.randint(0, 364)
    
    for i in range(0, 7):
        #mod it incase we get to the end of the array
        week.append(calendar[(random_index + i) % 365])
    
    return week


#list to store the dictionary result of each experiment and later we will go through and parse results
results = []


#we are going to run this experiment 1000 times
for i in range(225):
    print(str(i / 225) + " percent done")
     #generate 5 random weeks
    week1 = generate_random_week()
    week2 = generate_random_week()
    week3 = generate_random_week()
    week4 = generate_random_week()
    week5 = generate_random_week()

    #percentage of missing kids that go missing on any random 5 weeks
    week1_cases = count_missing_kids_week(week1, data_frame, 'missingSince')
    week2_cases = count_missing_kids_week(week2, data_frame, 'missingSince')
    week3_cases = count_missing_kids_week(week3, data_frame, 'missingSince')
    week4_cases = count_missing_kids_week(week4, data_frame, 'missingSince')
    week5_cases = count_missing_kids_week(week5, data_frame, 'missingSince')

    #use a dictionary to store corresponding total cases and percentage for each simulation
    total_5week = {}
    
    total_cases = week1_cases[0] + week2_cases[0] + week3_cases[0] + week4_cases[0] + week5_cases[0]
    total_percentage = week1_cases[1] + week2_cases[1] + week3_cases[1] + week4_cases[1] + week5_cases[1]
    
    #store each attribute to a dictionary
    total_5week["cases"] = total_cases
    total_5week["percentage"] = total_percentage


    #add to list
    results.append(total_5week)


print(results)
