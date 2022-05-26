'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

loop start with mainum = 1 
loop divider with 2 through 20
if not divisible (mainum % divider != 0):
    increment mainum

'''
# Brute force
# def smallest_multiple(n):
#     mainum = n
#     origin_n = n
#     while n > 1:
#         while mainum % n == 0:
#             if n == 1:
#                 print('------success-------')
#                 return mainum
#             n -= 1
#         mainum += 1
#         n = origin_n

# print(smallest_multiple(10)) # 2520
# print(smallest_multiple(20)) # 232792560

# Optimized
import math
# Create array of primes p
p = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
def sm_mult(n, p):
    k = n
    result = 1
    i = 1
    a = [i for i in range(i)]
    check = True
    limit = math.sqrt(k)
    while p[i] <= k:
        a[i].append(1) 
        if check:
            if p[i] <= limit:
                a[i].append(math.log(k) // math.log(p[i]))
            else:
                check = False
        result = result * p[i] ** a[i]
        i += 1
    return result

print(sm_mult(20, p))
