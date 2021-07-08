# Every number represents a color.
# Count the numbers to find the sum of colors. 

def colorCounter(nums):
    if not nums: 
        return []

    ar = {}
    for i in range(max(nums) + 1):
        count = 0
        ar[i] = count
        count += 1

    for i in range(len(nums)):
        ar[nums[i]] += 1

    return ar

numsArr = [3,2,3,4,5,5,6,6,7,8,5,4,3,1,2,2,2,2,2,3,4,5,6,6,2,2,3,1,1,5,5,6]

print(colorCounter(numsArr))

 