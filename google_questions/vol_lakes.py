'''
compute the volume of water that could be held in all lakes
given an array of heights of the bars
Example:
input: [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]
output: 15
explanation: 3 bodies of water; volumes 1,7,7 = 15
'''
'''
solution:
involving max values and difference between max and next value
find mid point and go to mid
find the end and go from end to mid repeat algo below
set max = 0
check if next > current and next >= max
  set next as max, go to next i
else next < current and next < max
  find difference, diff = diff + (max - next)
  go to next i
'''
def vol(arr):
    '''compute difference in nums if nums have smaller values in between 
    larger nums
    input: array of nums
    output: int as sum of differences
    '''
    mid = len(arr) // 2
    end = len(arr)-1
    max = 0
    diff = 0
    for i in range(mid): # Loop going forwards
      if arr[i+1] > arr[i] and arr[i+1] >= max: 
          max = arr[i+1]
          continue
      else:
          diff += max - arr[i+1]
    for i in range(end, mid, -1): # Loop going forwards
      if arr[i-1] > arr[i] and arr[i-1] >= max: 
          max = arr[i-1]
          continue
      else:
          diff += max - arr[i-1]
    return diff
# Testing
print(vol([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]))

def trap(height):
  # Keep track of pos of first and last numbers
  left_index, right_index = 0, len(height) - 1
  # Keep track of max num from left and right
  left_max, right_max = 0,0
  output = 0
  while left_index < right_index: # Until we cross over
    # Check if left num is smaller than right num
    if height[left_index] <= height[right_index]:
      # if yes, check if which is greater the arr num or left max 
      # and assign to left_max
      left_max = max(left_max, height[left_index])
      # add to output which is greater 0 or left max - arr num
      output += max(0, left_max - height[left_index])
      left_index += 1
    else: # right num is smaller than left num at index
      # Assign to right max which is greater prev right_max
      # or right index from num arr (height)
      right_max = max(right_max, height[right_max])
      # add to output which is greater? 0 or right max - arr num at right index
      output += max(0, right_max - height[right_index])
      right_index -= 1
    return output

'''
We are recording left pos and right pos (indexes) of both sides
when we traverse the arr, the smaller values in arr at positions go first
We are recording left and right max values, will be used to find lakes
and subtract the differences to writie to an output 
We are recording the output number which tells us the difference between
max num recorded previously and current (smaller) value of array 
As we inc and dec left and right respectively until they cross (when l = r)
Find smaller val in arr to determine who's going to next pos (index)
Find max val at index and record it to max var
Compare max num to current arr val if there's a diff, subtract smaller
num from max and add difference to output = lake, otherwise add 0 to output
'''