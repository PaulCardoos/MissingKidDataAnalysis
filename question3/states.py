"""
code for missing kids by state and compare with population to get percentage
written by Paul Cardoos and Danae Griffith
question 3
"""


import pandas as pd
import numpy as np
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
            "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
            "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
            "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PR","PA", "RI", "SC", 
            "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


#load csv file
data = pd.read_csv('../missingKids.csv')

#get relevant data (in this case missing Since and AgeNow)
data_frame = pd.DataFrame(data, columns=["state"])

#dictionary that contains missing kid per state
missing_kids = {}

#loop through states
for i in range(len(data_frame)):
    try:
        if missing_kids[data_frame["state"][i]]:
            missing_kids[data_frame["state"][i]] += 1
    except KeyError:
        missing_kids[data_frame["state"][i]] = 1

#store the missing kids number in an array
missing_kids_state = []
old = []

for i in missing_kids:
    #strip to normalize data
    if str(i).strip() in states:
        missing_kids_state.append(missing_kids[i])


#standard deviations of the amounts that went missing from each state
print("std : ", np.std(missing_kids_state))

#mean of the amount of kids taht went missing from each state
print("mean : ", np.mean(missing_kids_state))

#median of the amount of kids that went missing from each state
print("median : ", np.median(missing_kids_state))