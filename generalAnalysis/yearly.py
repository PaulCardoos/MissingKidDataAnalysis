import pandas as pd
import numpy as np


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
years = list(df["year"].unique())
df = df.groupby(["year"]).count()
s = pd.Series(data=df["firstName"])


#create bar plot
import matplotlib.pyplot as plt
fig = plt.figure()
plt.xticks( rotation=90 )
plt.title("Yearly Total Missing Kid Reports (Since 1971)")
plt.xlabel("Year") 
plt.ylabel("Total Missing Kids Reports") 
plt.bar(list(s.index),list(s))
plt.show()

#create another bar plot
