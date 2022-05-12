'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 20
5 3 1
-9 8 54

returns absolute| ( 1+3+54 ) - ( 20+3-9 ) |
'''

def diagonalDifference(arr):
    p_diag = []
    s_diag = []
    p_pos = 0
    s_pos = len(arr)-1
    for i in range(len(arr)):
        p_diag.append(arr[i][p_pos])
        s_diag.append(arr[i][s_pos])
        p_pos += 1
        s_pos -= 1
    
    return abs(sum(p_diag)-sum(s_diag))
        

matrix = [
    [15, 5, 32, 53],
    [3, 11, 7, 21],
    [8, -3, 4, 14],
    [9, -2, -11, 54]
]
print(diagonalDifference(matrix))


def plusMinus(arr):
    # Input: array of positive, negative, and zero integers
    # Output: the ratio count of each integer rounded to 6 digit precision float
    total = len(arr)
    pos_count, neg_count, zero_count = 0,0,0
    
    for i in arr:
        if i > 0:
            pos_count += 1
        elif i < 0:
            neg_count += 1
        else:
            zero_count += 1
    
    pos_ratio = round(float(pos_count / total), 6)
    neg_ratio = round(float(neg_count / total), 6)
    zero_ratio = round(float(zero_count / total), 6)
    
    p_print = print(pos_ratio, '\n', neg_ratio, '\n', zero_ratio)
    return p_print

plusMinusArray = [4, -3, 0, 0, 0, 0, 0, 0, 0, 3, 5, 10, 100, -32, -342, 5, -5]
plusMinus(plusMinusArray)

