#import pandas 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load csv file
data = pd.read_csv('missingKids.csv')

#get relevant data (in this case missing Since and AgeNow)
data_frame = pd.DataFrame(data, columns=["height", "firstName"])

#function to get height in inches
def get_height_in_inches(feet, inches):
    return feet * 12 + inches

#store all the heights in an array
all_heights = []

for i in range(len(data_frame)):
    try:
        #height and inches from csv 
        dimensions = str(data_frame["height"][i]).split("'")
        feet = int(dimensions[0])
        inches_str = dimensions[1]
        inches = int(inches_str[0:len(inches_str) - 1])
       
        #convert to height in inches and store into an array
        height_in_inches = get_height_in_inches(feet, inches)
        all_heights.append(height_in_inches)

        
    except:
        pass

#the amount of records that have heights is the length of the array      

#print(len(all_heights))

#minimum height of kid that went missing
print(np.min(all_heights))

#tallest kid that went missing
print(np.max(all_heights))

#standard deviations of the heights of the kids that went missing
print(np.std(all_heights))

#average of the heights of the kids that went missing
print(np.mean(all_heights))

#median of the heights from the kids that went missing
print(np.median(all_heights))

#boxplot
plt.boxplot(all_heights)
plt.show()