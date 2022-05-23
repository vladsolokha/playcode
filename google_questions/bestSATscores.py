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
d = {DSST: [800, 300], Google: [1000, 200], IBM: [1400, 500]}
sum = 0
for key,val in enumerate(d.items):
    sum += val

return key of max value in company
'''

def bestAvgSat(objData):
    # record data in dict
    for key,val in enumerate(objData.items):
        key = sum(val/len(val))
    return max(key)


d = {DSST: [800, 300], Google: [1000, 200], IBM: [1400, 500]}