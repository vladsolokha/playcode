'''
There is a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. 
The player can jump on any cumulus cloud having a number that is 
equal to the number of the current cloud plus 1 or 2. 
The player must avoid the thunderheads. 
Determine the minimum number of jumps it will take to jump from the 
starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe 
or 1 if they must be avoided.
'''

def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    pos = 0
    i_range = len(c)-1
    while pos < i_range: 
        if pos+1 == i_range:
            jumps += 1
            break 
        if c[pos+2] == 0:
            jumps += 1
            pos += 2
        else:
            jumps += 1
            pos += 1
    return jumps

test1 = [0,0,0,1,0,0,0,0]
test2 = [0,1,0,0,1,0,0,0]
test3 = [0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0]

print(jumpingOnClouds(test1))
print(jumpingOnClouds(test2))
print(jumpingOnClouds(test3))