'''
Given CSV file with 1000s of following:

Name, Company, SAT score
vlad, DSST, 800
sonny, Google, 1000
bob, Google, 200
brian, DSST, 300
patty, IBM, 1400
jerry, IBM, 500

output: the company that has the highest average score

ignore names
for each company, record count of co and add to score for that co
in dictionary
d = {company: [sum_score, count], company: [sum_score, count]}
d = {DSST: [800, 300], Google: [1000, 200], IBM: [1400, 500]}
max_company = first record from d.company, sum/count
max_score = score corresponding to the max_company
for key,val in enumerate(d.items):
    sum += val
return key of max value in company
'''
import csv
file = open('satData.csv')
csvreader = csv.reader(file)
header = [next(csvreader)]
d = {}
# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
def bestAvgSat(objData):
    # record data in dict
    for key,val in enumerate(objData.items):
        key = sum(val/len(val))
    return max(key)


d = {DSST: [800, 300], Google: [1000, 200], IBM: [1400, 500]}