"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

# Pop out first number from list, then iterate through array and
# compare sum of popped element with each item in list to target value.
# if no target sum, append item back into array and iterate popping next item

def sum_in_list (arr, k):
    for list_number in arr:
        for next_number in arr:
            print(list_number)
            print(next_number)
            if  == k:
                return True
    return False

numbers_list = [10, 15, 3, 7]
target = 17
print(sum_in_list(numbers_list, target))

