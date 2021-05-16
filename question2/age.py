"""
Code to generate statistics about age kids went missing

written by Paul Cardoos and Aanab Nehala 
question 2
"""

#code to find standard deviation, median, mean, average of age when kids went missing

#import pandas for data manipulation
import pandas as pd

#import Counter to get frequency
from collections import Counter

#import numpy to check for nan
import numpy as np

#load csv file
data = pd.read_csv('../missingKids.csv')

#get relevant data (in this case missing Since and AgeNow)
data_frame = pd.DataFrame(data, columns=["firstName", "missingSince", "ageNow"])


#array to store the age the children went missing
age_went_missing = []

for i in range(len(data_frame)):
    try:
        #get the year that the child went missing
        year = str(list(data_frame["missingSince"])[i]).split(", ")[1]
        
        #the age the child would be now
        age = (list(data_frame["ageNow"])[i])

        #check for nan or if age is 0 or 
        if np.isnan(age) or age == 0:
            #if nan (not a number) continue to next iteration
            continue
        
        #get how long the child has been missing and subtract from ageNow
        how_long_missing = 2021 - int(year)
        
        #get age missing and store to array
        age_missing = age - how_long_missing

        #if age is -1 then the child is 1 when they went missing
        if age_missing == -1 :
            age_missing = 1
        #if age is less than zero idk so dont count this data
        elif age_missing < 0:
            continue
        #else data is valid
        else:
            pass
  
        age_went_missing.append(age_missing)

    except:
        pass

#get the count of how many kids went missing at each age
age_went_missing_count = Counter(age_went_missing)
print(len(age_went_missing_count))
print("Number of kids that went missing at each age: " , age_went_missing_count)

#a dictionary to keep the percentages for each kid that went missing
age_went_missing_percent = {}

#calculate percentage and store in dictionary
for i in age_went_missing_count:
    percentage = age_went_missing_count[i] / 4704
    age_went_missing_percent[i] = percentage * 100

print("percent: " , age_went_missing_percent)