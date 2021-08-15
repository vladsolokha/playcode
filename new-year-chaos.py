'''
Given queue from 1 to n. Any number can switch with 
a number to the left of queue

One n can bribe at most two others. Bribes > 2 = Too chaotic. 

Determine min number of bribes that took place 
to get to given queue order.

Print number of bribes, or, if anyone has bribed more than 2 people, 
print 'Too chaotic'

example
q = [1,2,3,4,5,6,7,8] person 5 bribes 4, the q will look like
q = [1,2,3,5,4,6,7,8] => return 1

q = [4,1,2,3] person 4 had to bribe 3 people. Print 'Too chaotic'
'''
q = [2, 1, 5, 3, 4]
q2 = [1,2,3,5,4,6,7,8]
q3 = [4,1,2,3]

def minimumBribes(q):
    p = '\nToo chaotic'
    difference = 0 # Tells us bribe happened
    bribes_count = 0
    
    for n in range(len(q)-1): #if using n+1 need range to be q-1
        difference = q[n] - q[n+1]
        
        if difference > 0:
            bribes_count += difference

        if difference > 2:
            too_chaotic = str(bribes_count) + p
            return too_chaotic
            break
        
    return bribes_count

print(minimumBribes(q))
print(minimumBribes(q2))
print(minimumBribes(q3))
