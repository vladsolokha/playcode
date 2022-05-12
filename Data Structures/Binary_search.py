
#need a list of sorted names
#can use quick sort to do this
#need a list of names to search and match 
names = ['a','b','c','d','e','f','g']
name = ['c', 'a']

def binary_search(data, target):
    first = 0
    last = len(data) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if data[midpoint] == target:
            return midpoint
        elif data[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint -1
    return None

for name in names:
    position = binary_search(names, name)
    print(position)
