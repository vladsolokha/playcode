# Traverse through an array and search for match 
names = ['a','b','c','d','e','f','g']
name = ['c', 'a']
def position_of_result(data, target):
    for position in range(0, len(data)):
        if target == data[position]:
            return position
    return None

for name in names:
    position = position_of_result(names, name)
    print(position)

