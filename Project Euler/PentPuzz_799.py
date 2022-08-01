'''
Pentagonal numbers are generated by
P(n) = 1/2 * n * (3 * n - 1)
giving the sequence
1, 5, 12, 22, 35, 51, 70, 92, ...
Some pentagonal numbers can be expressed by sum of 2 other pentagonal numbers
P(8) = 92 = 22 + 70 = P(4) + P(7)
3577 is smallest pentagonal number that can be expressed as sum of 
two pentagonal numbers 2 different ways:
P(49) = 3577 = 3432 + 145 = P(48) + P(10)
               3290 + 287 = P(47) + P(14)
107602 is smallest pentagonal number that can be expressed as sum of 
two pentagonal numbers 3 different ways.

find the smallest pentagonal number that can be expressed as sum of 
two pentagonal numbers in over 100 different ways

create function to get list of pentagonal numbers
start from smallest target number
first number = 0
last number = -1
while target didn't reach end of list <= len(p)-1:
    while last number didn't reach available 102 
        while first p of number < p of last
            last number (-1) + first number (0) = sum of two pentagonal numbers
            if sum is == target number then
                count inc, found count matching sum 
                print found count sum of last number and first number 
                last number - 1 to go to next last number
                first number has to be greater than where prev sum was found
            else: try another first number + 1
        last number reached all available 102 to add to firsts
        reset last number = -1
        reset first number = 0
    increase target number + 1 until end of list is reached
    count = 0 resets count for another target number
    target number reached end of list
'''
def pent_List(n):
    a = []
    for i in range(1, n+1):
        a.append(int(1/2 * i * ( 3 * i - 1 )))
    return a
p = (pent_List(15000))
print(p[len(p)-1])
first, first_saved = 0,0
target = len(p)-1
last = target-1
count = 0
while target >= 1:
    while first < last:
        if p[first] + p[last] == p[target]:
            print('p(',first+1,')+p(',last+1,')=p(',target+1,')')
            count += 1
            last -= 1 
            first += 1
        else:
            first += 1 
    if count >= 1:
        print('count for ', p[target], ', at p(', target+1, ') is ', count)
    target -= 1
    last -= 1
    first = 0
    count = 0