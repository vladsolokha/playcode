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
def findprimes(n):
    primes = [2]
    for i in range(3, n+1):
        for j in primes:
            if j == primes[len(primes)-1]:
                primes = primes + [i]
            if i % j == 0:
                break
            else:
                continue
    return primes

print(findprimes(100))

def findfactors(n):
    primes = findprimes(n)
    factors = []
    for i in range(n):
        for j in range(i,n):
            if i * j == n: 
                if i not in primes:
                    if j not in primes:
                        factors = findfactors(i) + findfactors(j)
                    else:
                        factors = [j] + findfactors(i)
                else:
                    if j not in primes:
                        if i not in primes:
                            factors = findfactors(i) + findfactors(j)
                        else:
                            factors = [i] + findfactors(j)
                    else:
                        factors = [i,j]
                break
    if n in primes:
        factors = [n]
    return factors

def findsmallest(n):
    primes = findprimes(n)
    primesnum = [0] * len(primes)
    allzefac = []
    for i in range(n+1):
        allzefac = allzefac + [findfactors(i)]
    for i in primes:
        for j in allzefac:
            if j.count(i) > primesnum[primes.index(i)]:
                primesnum[primes.index(i)] = j.count(i)

    summy = 1
    print('primes: ',primes)
    print('prime sum nums: ', primesnum)
    for i in range(len(primes)):
        if primesnum[i] != 0:
            summy = summy * primes[i] ** primesnum[i]
    return summy

print(findsmallest(200))

# resource 
# mickyhowells https://projecteuler.net/thread=5;page=3#4213
'''
Upon reading more discussions
there's a formula
calculate all primes
use the primes and multiply them to get to answer
use lowest common multiples and their prime factorizations
to get highest degree of each prime
f(n) = LCM(1,2,...,n) = for every p <= n, p^(log(n)//log(p)), p is prime
n is the number we put into the function. 
f(20) = 2^(log(20)//log(2)) * 3^(log(20)//log(3)) * 5^(log(20)//log(2)) ... *19
= 232792560
'''
import math
def isPrime(p):
    prime = 1
    check = 2
    while prime == 1 and check <= math.sqrt(p):
        if p % check == 0:
            prime = 0
        check += check % 2 + 1
    return prime == 1

def f(n):
    if n == 1:
        return 1
    else:
        product = 2 ** int(math.log(n) / math.log(2))
        k = 3
        while k <= n:
            if isPrime(k):
                product *= k ** int(math.log(n) / math.log(k))
            k += 2
        return product

print(f(20))