print('How many cats do you own?')
numberOfCats=input()
try:
    if int(numberOfCats) <=3 and int(numberOfCats) >=0:
        print('You really dont like cats as much as I though you would be')
    if int(numberOfCats) <=-1:
        print("c'mon, dont tell me you are constantly losing cats.")
except:
    print('Hon, please enter a valid number.')
