import pandas as pd
import numpy as np
from scipy import stats
from monthDay import weeks


"""
the holiday weeks are defined as follows

week 1 (New Years)
week 27 (July 4th)
week 44 (Halloween)
week 47 (Thanksgiving)
week 52 (Christmas)
"""
# load data
df = pd.read_csv("../missingKids.csv")

# clean out data points that have 3 or more nans
df.dropna(axis=0, thresh=3, inplace=True)

# delete columns that I do not want
df.drop('_id', inplace=True, axis=1)
df.drop('image', inplace=True, axis=1)
df.drop('middleName', inplace=True, axis=1)
df.drop('details', inplace=True, axis=1)

#modify the missingSince column to work with in python
#change format from Apr 6, 2007 to just Apr 6
df["missingSince"] = df["missingSince"].apply(lambda x :str(x).split(",")[0])

#group each day to get the total missing reports each day
df = df.groupby(["missingSince"]).count()

#convert to series with data as index and total missing kid report for that day
s = pd.Series(data=df["firstName"])

missing_kid_report = {}
for day in s.iteritems():
    missing_kid_report[day[0]] = day[1]


total_per_week = [0] * 53

#calculate total per week 
for num, week in enumerate(weeks):
    total_reports = 0
    for day in week:
        total_reports += missing_kid_report[day]
    
    #store total reports in match index for the week
    total_per_week[num + 1] = total_reports

#display total per week
for i, week in enumerate(total_per_week):
    print("week " + str(i) + " : " + str(week))   

#the index of holiday weeks in total_per_week
holidays = [0,1,27,44,47,52]

#seperate holiday weeks from the rest of the week
holiday_weeks = [total_per_week[1], total_per_week[27], total_per_week[44], total_per_week[47], total_per_week[52]]
the_rest = [i for i in total_per_week if i not in holidays]


#import scipy stats to do the welches-t test from the wikipedia document you gave
print(stats.ttest_ind(the_rest, holiday_weeks, equal_var = False))