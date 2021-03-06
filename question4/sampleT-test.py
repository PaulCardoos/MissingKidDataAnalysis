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
df["year"] = df["missingSince"].apply(lambda x :str(x).split(",")[1])
df["missingDate"] = df["missingSince"].apply(lambda x :str(x).split(",")[0])
df.drop('missingSince', inplace=True, axis=1)

df = df[(df["year"].astype(int) > 2019) & (df["year"].astype(int) < 2021)]

#group each day to get the total missing reports each day
df = df.groupby(["missingDate"]).count()
#print(df)

#convert to series with data as index and total missing kid report for that day
s = pd.Series(data=df["firstName"])

#created a dictionary to store weekly total for missing kid reports in 2020
missing_kid_report = {}

for day in s.iteritems():
    missing_kid_report[day[0]] = day[1]


total_per_week = [0] * 53

#calculate total per week 
for num, week in enumerate(weeks):
    total_reports = 0
    for day in week:
        try:
            total_reports += missing_kid_report[day]
        except KeyError:
            pass

    #store total reports in match index for the week
    total_per_week[num + 1] = total_reports

#display total per week
for i, week in enumerate(total_per_week):
    print("week " + str(i) + " : " + str(week))   

#the index of holiday weeks in total_per_week
holidays = [0,1,27,44,47,52]

#seperate holiday weeks from the rest of the week
holiday_weeks = [total_per_week[1], total_per_week[27], total_per_week[44], total_per_week[47], total_per_week[52]]
holiday_mean = sum(holiday_weeks)/(len(holiday_weeks) - 1)

print("Holiday weeks : ", holiday_weeks)
the_rest = [i for i in total_per_week if i not in holidays]
the_rest_mean =  sum(the_rest)/len(the_rest)
print("Rest of the weeks mean : ", the_rest_mean)

import matplotlib.pyplot as plt
# Make a random dataset:
height = [holiday_mean, the_rest_mean]
bars = ('Holidays', 'Rest of the year')
y_pos = np.arange(len(bars))
# Create bars
plt.title("2020 Avg Number Missing Reports Over Holidays vs Rest of the Year")
plt.ylabel("Average Number of Missing Kids Reported")
plt.bar(y_pos, height, color="green", width=.7)

# create names on the x-axis
plt.xticks(y_pos, bars)
# Show graphic
plt.show()


#import scipy stats to do the welches-t test from the wikipedia document
print(stats.ttest_ind(the_rest, holiday_weeks, equal_var = False))