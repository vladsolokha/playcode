# Given a string of letters representing path, U = up and D = down
# A hiker is taking steps for each letter
# Starts at sea level and ends at sea level
# Return an int that determines how many valleys he went down into below sea level

# If he goes below sea level, he's in a valley = 1, if he never returns to sea level valley is still = 1
# If he goes above sea level, its a mountain, and then goes to a valley below sea level into valley, valley = 2

# have int represent + if above sea level and - below sea level called height or h
# += if up and -= if down
# we need to count the number of times number went from 0 to a negative value
def hikerValleys(steps, path):
    height = 0 # can be neg or pos
    valleyCount = 0 #count everytime h becomes <= 0
    for step in path:
        if step == "U":
            height += 1
        if step == "D": 
            height -= 1
        if step == "U" and height == 0: #this needs true condition only if h became 0 (we're out of valley) when step is U
            valleyCount += 1
            
    return valleyCount

# For some cases -1 appeared  more than once, therefore if failed the test because 
# it didn't move from 0 to -1 but moved from -2 to -1 which was an 'U' char

path = 'UDDDUDUU'
path2 = 'DUDDDUUDUU'
walk = len(path)
walk2 = len(path2)

print(hikerValleys(walk, path))
print(hikerValleys(walk2, path2))
