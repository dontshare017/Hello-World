print('Wassup!')
print('What should I call you?')
UserName= input()

print('Alrighty, ' + UserName + ', I want to introduce you to a game.')
print('''It's really easy. I have a number in mind, it could be anywhere between 1-20. You have to guess the number
within 7 tries. That's plenty of chances.''')
print('If you dont get it then you are a little dummy >:^).')
print('Now lets begin.')

import random
secretNumber = random.randint(1,20)

print('What is your guess?')

for NumberofTries in range(1,8):
    guesses=input()
    try:
        if int(guesses) < secretNumber:
            print('Ah. Nah. That number is too low. Try again')
        elif int(guesses) > secretNumber:
            print('What? Thats too high. Dont go that far >:^O')
        elif int(guesses) == secretNumber:
            break
    except:
        print('Can you read?? I wanted you to guess a number, not a word! ')

if int(guesses)== secretNumber and NumberofTries == 7:
    print('Well well well, gotta say, thats much better than I expected, ' + UserName + '.')
    print('You guessed the number in ' + str(NumberofTries) + ' tries. Nice Job.')
    print('Now close this program and get a life.')
elif int(guesses) == secretNumber and NumberofTries < 7:
    print('Excuse me?? How can you guess it in just ' + str(NumberofTries) + ' times?? @Harvard please accept')
else:
    print('The number I had in mind was ' + str(secretNumber) + ', but your tries are used up.')
    print('You are a failure ahaha')

import os
os.system('pause')
