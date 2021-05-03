"""
some code that generate 5 random weeks out of year and get the amount of kids
that were reported missing each week and the total percentage of the cases that
the cases during the 5 random weeks account for
"""
#import array from separte file and random to generate random day
import pandas as pd
from monthDay import calendar
from holiday import count_missing_kids_week
import random

#read data from the csv
data = pd.read_csv('missingKids.csv')

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
for i in range(75):
    print(str(i / 75) + " percent done")
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

#the results from 75 tests
results_from_75_tests = [{'cases': 439, 'percentage': 8.689627870150435}, {'cases': 486, 'percentage': 9.619952494061758}, {'cases': 332, 'percentage': 6.571654790182106}, {'cases': 397, 'percentage': 7.858273950910531}, {'cases': 524, 'percentage': 10.37212984956453}, {'cases': 508, 'percentage': 10.055423594615993}, {'cases': 808, 'percentage': 15.99366587490103}, {'cases': 454, 'percentage': 8.986539984164688}, {'cases': 1029, 'percentage': 20.36817102137767}, {'cases': 1178, 'percentage': 23.317498020585905}, {'cases': 862, 'percentage': 17.06254948535234}, {'cases': 475, 'percentage': 9.402216943784639}, {'cases': 483, 'percentage': 9.560570071258907}, {'cases': 471, 'percentage': 9.323040380047505}, {'cases': 1267, 'percentage': 25.079176563737132}, {'cases': 590, 'percentage': 11.678543151227236}, {'cases': 1632, 'percentage': 32.304038004750595}, {'cases': 744, 'percentage': 14.726840855106888}, {'cases': 753, 'percentage': 14.90498812351544}, {'cases': 910, 'percentage': 18.01266825019794}, {'cases': 549, 'percentage': 10.866983372921615}, {'cases': 650, 'percentage': 12.866191607284245}, {'cases': 577, 'percentage': 11.421219319081551}, {'cases': 1399, 'percentage': 27.69200316706255}, {'cases': 733, 'percentage': 14.50910530482977}, {'cases': 1002, 'percentage': 19.833729216152015}, {'cases': 471, 'percentage': 9.323040380047505}, {'cases': 661, 'percentage': 13.083927157561362}, {'cases': 511, 'percentage': 10.114806017418845}, {'cases': 836, 'percentage': 16.547901821060965}, {'cases': 742, 'percentage': 14.687252573238322}, {'cases': 793, 'percentage': 15.696753760886779}, {'cases': 578, 'percentage': 11.441013460015835}, {'cases': 1264, 'percentage': 25.019794140934287}, {'cases': 670, 'percentage': 13.262074425969914}, {'cases': 1341, 'percentage': 26.54394299287411}, {'cases': 700, 'percentage': 13.855898653998418}, {'cases': 1001, 'percentage': 19.81393507521774}, {'cases': 935, 'percentage': 18.507521773555027}, {'cases': 1033, 'percentage': 20.447347585114805}, {'cases': 768, 'percentage': 15.201900237529692}, {'cases': 509, 'percentage': 10.075217735550277}, {'cases': 815, 'percentage': 16.132224861441014}, {'cases': 1205, 'percentage': 23.851939825811556}, {'cases': 1427, 'percentage': 28.246239113222487}, {'cases': 624, 'percentage': 12.351543942992874}, {'cases': 1155, 'percentage': 22.862232779097386}, {'cases': 574, 'percentage': 11.361836896278701}, {'cases': 575, 'percentage': 11.381631037212985}, {'cases': 568, 'percentage': 11.243072050673}, {'cases': 533, 'percentage': 10.550277117973081}, {'cases': 1277, 'percentage': 25.27711797307997}, {'cases': 632, 'percentage': 12.509897070467142}, {'cases': 1065, 'percentage': 21.08076009501188}, {'cases': 761, 'percentage': 15.063341250989707}, {'cases': 487, 'percentage': 9.63974663499604}, {'cases': 824, 'percentage': 16.310372129849565}, {'cases': 641, 'percentage': 12.688044338875692}, {'cases': 609, 'percentage': 12.054631828978621}, {'cases': 985, 'percentage': 19.497228820269203}, {'cases': 736, 'percentage': 14.568487727632622}, {'cases': 410, 'percentage': 8.115597783056215}, {'cases': 785, 'percentage': 15.53840063341251}, {'cases': 1607, 'percentage': 31.80918448139351}, {'cases': 1416, 'percentage': 28.028503562945367}, {'cases': 432, 'percentage': 8.551068883610451}, {'cases': 455, 'percentage': 9.00633412509897}, {'cases': 450, 'percentage': 8.907363420427554}, {'cases': 528, 'percentage': 10.451306413301662}, {'cases': 999, 'percentage': 19.77434679334917}, {'cases': 432, 'percentage': 8.551068883610451}, {'cases': 366, 'percentage': 7.244655581947743}, {'cases': 792, 'percentage': 15.676959619952495}, {'cases': 415, 'percentage': 8.214568487727632}, {'cases': 1172, 'percentage': 23.198733174980205}]
