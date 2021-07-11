# Given a string of letters representing path, U = up and D = down
# A hiker is taking steps for each letter
# Starts at sea level and ends at sea level
# Return an int that determines how many valleys he went down into below sea level

# If he goes below sea level, he's in a valley = 1, if he never returns to sea level valley is still = 1
# If he goes above sea level, its a mountain, and then goes to a valley below sea level into valley, valley = 2

# have int represent + if above sea level and - below sea level called height or h
# += if up and -= if down
# we need to count the number of times number became -
def hikerValleys(steps, path):
    h = 0
    valley = 0
    for i in range(steps):
        
    return valley 


path = 'UDDDUDUU'
walk = len(path)

print(hikerValleys(walk, path))