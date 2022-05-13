'''
h-index is a metric used to calculate impact of researcher's papers.
Calculated as:
A researcher has index h if at least h of her N papers have h citations each.
If there are multiple h satisfying this formula, the maximum is chosen.
(* start from the largest)

ie
N = 5 and arr = [4, 3, 0, 1, 5], so h-index = 3
The researcher has 3 papers of at least 3 citations.

It is true that there are h many items in arr that are >= 3 (h). 

1. assign max num from array to h
2. initialize a count variable to count how many numbers that are in 
arr that are greater than or equal to h
3. count how many numbers in arr that are >= h
4. check if count is >= h 
5. when count becomes >= h break the loop
6. otherwise decrement h by 1
7. repeat at step 2
'''
arr = [4, 3, 0, 1, 5]
count = 0
h = max(arr)+1
print('h at max is ', h)
while count <= h:
  count = 0
  print('h is ', h, ' count is ', count)
  for i in arr:
    print('compare if ', i, ' is greater than ', h) 
    if i >= h:
      print(i, ' is >= ', h, ' increase count')
      count += 1
      print('count is ', count)
    else:
      print(i, ' is not greater than ', h, ' continue loop')
  if count >= h:
    print('h is: ', h)
    break
  h-=1