'''
given 6x6 2D arr
an hourglass is subset of arr
there are 16 hourglasses in arr

eval the sum of each hourglass
print the maximum hourglass sum

arr =
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

there the 16 hourglass sums are
-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18

the highest sum is 28 from hourglass beginning at row 1, column 2:
0 4 3
  1
8 6 6
'''

hg = [
    [1, 1, 1, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0], 
    [1, 1, 1, 0, 0, 0], 
    [0, 0, 2, 4, 4, 0], 
    [0, 0, 0, 2, 0, 0], 
    [0, 0, 1, 2, 4, 0]
]
# ans 19
hg2 = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 9, 2, -4, -4, 0], [0, 0, 0, -2, 0, 0], [0, 0, -1, -2, -4, 0]]
# ans 13
hg3 = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]
# ans 28

def hourglassSum(arr):
    hourglass_total_list = []
    for column in range(4):
      for row in range(4):
        top_row = arr[column][row] + arr[column][row+1] + arr[column][row+2]
        mid_row = arr[column+1][row+1]
        end_row = arr[column+2][row] + arr[column+2][row+1] + arr[column+2][row+2]
        total_hourglass = top_row + mid_row + end_row
        hourglass_total_list.append(total_hourglass)
    return max(hourglass_total_list)

print(hourglassSum(hg))
print(hourglassSum(hg2))
print(hourglassSum(hg3))


