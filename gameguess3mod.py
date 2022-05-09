from sys import stdin as ask
from random import randint as randomizer
from time import sleep as wait
counter = 0

print('Welcome\nWhat\'s your name?')
name= ask.readline() 
wait(2) 
print('Well hello to you, too %s' % name)
wait(2)
print('Let\'s play guess my number\nGuess 0-10 below:')

def makeRandNum():
    randnum = randomizer(0,10) 
    return randnum

def guessagain():
    guess = ask.readline()
    guess.rstrip('\n')
    return int(guess)


def checker():
    global counter
    randnum = makeRandNum()
    guess = guessagain()
    print(randnum)
    if guess == randnum:
        wait(2)
        print('You did it! It only took you %d tries' %counter)
    elif guess > randnum:
        wait(2)
        print('You\'re too high!')
        guessagain()
        counter += 1
    elif guess < randnum:
        wait(2)
        print('You\'re too low!')
        guessagain()
        counter += 1         

def run():       
    rungame = True
    while rungame:
        checker() 
        print('Would you like to play again? y or n')
        playagain = ask.readline() 
        playagain.rstrip() 
        if playagain == 'y':
            checker()
            
        else:
            rungame = False      
            print('Thanks for playing! Bi Now!\nGame Over')
            break

run()
