'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

starting at 999 going to 899, backwards
do for loop in for loop to produce multiplication
check result reads the same forwards and backwards
'''
for i in range(999, 899, -1):
    for j in range(999, 899, -1):
        result = i * j
        backwards_result = str(result)[::-1]
        if str(result) == backwards_result:
            print('---------------------Success!!!')
            print(result)
            break

# result
# 906609