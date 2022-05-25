# Using pandas API
# reference: https://pandas.pydata.org/docs/reference/api/
import pandas as pd
# get data from csv and organize in DataFrame (table)
data = pd.read_csv("google_questions\satData.csv")
print('All data from .csv\n', data)
# group data by Company and with SAT means (averages)
d = data.groupby('Company', sort=False).mean()
print('Company Average SAT scores\n', d)
# get company with the maximum mean
m = d.idxmax(axis=0)
print('Company with highest average SAT scores\n', m)
# return company with highest maximum mean
r = m.iloc[0]
print('Company with highest average SAT scores = ', r)

'''
Given CSV file:

Name,Company,SAT
vlad,DSST,800
sonny,Google,1000
bob,Google,200
brian,DSST,300
patty,IBM,1400
jerry,IBM,500
tre,DSST,900
rob,Top,1600
eric,Bottom,500

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