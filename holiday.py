#the main holiday dates christmas, haloween, new years, independence day and thanksgiving
halloween = ["Oct 31", "Nov 1", "Nov 2", "Nov 3", "Nov 4", "Nov 5","Nov 6"]
christmas = ["Dec 25", "Dec 26", "Dec 27", "Dec 28", "Dec 29", "Dec 30"]
new_years = ["Dec 31", "Jan 1", "Jan 2", "Jan 3", "Jan 4", "Jan 5", "Jan 6"]
thanksgiving = ["Nov 22",  "Nov 23", "Nov 24", "Nov 25", "Nov 26", "Nov 27", "Nov 28"]
fourth_of_july = ["Jul 4", "Jul 5", "Jul 6", "Jul 7", "Jul 8", "Jul 9", "Jul 10"]


def count_missing_kids_week(weeks, data_frame, col_name = ""):
    """
    params: weeks -> List
            all_datas -> pandas data frame
    description : a function that takes holiday dates and data frame and return 
    the number and percentage of kid that go missing on a holiday
    """
    count  = 0
    for i in range(len(weeks)):

        for j in range(len(data_frame)):
            if weeks[i] in str(list(data_frame[col_name])[j]):
                count += 1

    return count, 100 * count / len(data_frame)

#percentage of missing kids that go missing on halloween
# halloween_cases = count_missing_kids_week(halloween, data_frame, 'missingSince')
# print ('Halloween cases: ', halloween_cases[0])
# print ('Halloween cases percent: ', halloween_cases[1])

#percentage of missing kids that go missing on christmas
# Christmas_cases = count_missing_kids_week(christmas, data_frame, 'missingSince')
# print ('Christmas cases: ', Christmas_cases[0])
# print ('Christmas cases percent: ', Christmas_cases[1])

#percentage of missing kids that go missing on new years
# newyears_cases = count_missing_kids_week(new_years, data_frame, 'missingSince')
# print ('New Years cases: ', newyears_cases[0])
# print ('New Years cases percent: ', newyears_cases[1])

#percentage of missing kids that go missing on thanksgiving
# thanksgiving_cases = count_missing_kids_week(thanksgiving, data_frame, 'missingSince')
# print ('Thankgiving cases: ', thanksgiving_cases[0])
# print ('Thankgiving cases percent: ', thanksgiving_cases[1])

#percentage of missing kids that go missing on july 4
# jul4_cases = count_missing_kids_week(fourth_of_july, data_frame, 'missingSince')
# print ('Fourth of July cases: ', jul4_cases[0])
# print ('Fourth of July cases percent: ', jul4_cases[1])
