'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

given n, write function to print all prime factors of n
12 = '2 2 3' 
315 = '3 3 5 7'

steps
1. while n is divisible by 2, print 2 and divide n by 2
2. after step 1, n must be odd, start loop from i=3 to square root of n. While i divides n, print i and divide n by i, inc i by 2 and continue
3. if n is prime number and > 2, then n will not become 1 by above 2 steps; print n if it is > 2
'''

import math
from tkinter import N
test_n = 13195
problem_n = 600851475143
def prime_factors(n):
    sum = 0
    arr = []
    # Put the two's that divide n into sum and arr
    while n % 2 == 0:
        sum += 2
        arr.append(2)
        n /= 2
    # Since n is odd, skip of 2 can be used (3,5,7,...)
    for i in range(3, int(math.sqrt(n))+1, 2):
        # While i divides n, put i into sum and arr and divide
        while n % i == 0:
            sum += i
            arr.append(i)
            n /= i
    # Check if n is prime greater than 2
    if n > 2:
        sum += n
        arr.append(n)

    print('arr is ', arr)
    print('sum is ', sum)

prime_factors(test_n)
prime_factors(problem_n)