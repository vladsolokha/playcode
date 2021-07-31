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