# Given an array of letters, U = up and D = down
# A hiker is taking steps for each letter
# Starts at sea level and ends at sea level
# Return an int that determines how many valleys he went down into below sea level

# If he goes below sea level, he's in a valley = 1, if he never returns to sea level valley is still = 1
# If he goes above sea level, its a mountain, and then goes to a valley below sea level into valley, valley = 2

def hikerValleys(steps, path):
    valley = 0
    return valley 


path = [U,D,D,D,D,U,U,U,D,D,U,U,U,U,U,U,D,D,D,D,D,D,U,D,D,U,D,U,U,D,U,U,U,U,D,D,U,U,D]
walk = len(path)

print(hikerValleys(walk, path))