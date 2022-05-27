'''
sum of squares of first 10 natural numbers
1**2+2**2+3**2+...+10**2 = 385
square sum of first 10 natural numbers
(1+2+3+4+...+10)**2 = 55**2 = 3025
the difference between sum of squares and square of of sum is
3025 - 385 = 3025

find the difference between sum of squares of first 100 natural numbers
and the square of the sum

create function to square each of the 100 numbers and sum them
create function to sum first 100 numbers and then square them
subtract the functions
'''
def sumOfSquares(n):
    result = 0
    for i in range(n+1):
        result += i ** 2
    return result

def squareSum(n):
    result = 0
    for i in range(n+1):
        result += i
    return result ** 2

diff = squareSum(100) - sumOfSquares(100)
print(diff)