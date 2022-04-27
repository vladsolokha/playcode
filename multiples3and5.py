'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
def mult_of_3_and_5(goal):
    count = 0
    addition = 0
    for i in range(goal):
        if i == 0:
            continue
        if i % 3 == 0:
            print(i, ' is multiple of 3')
            count += 1
            addition += i
        if i % 5 == 0:
            print(i, ' is multiple of 5')
            count += 1
            addition += i
    return print('count is %d and sum of multiples is %d' % (count, addition))

print(mult_of_3_and_5(10))
#print(mult_of_3_and_5(100))
#print(mult_of_3_and_5(1000))
