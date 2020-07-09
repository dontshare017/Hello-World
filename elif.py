print('Hello')
print('What is your name?')
name=input()

if name.lower() == 'yifei':
        print('Wassup My Dude')

while name != 'yifei':
    print('You will be given another chance. What is your name?')
    name = input()
    if name.lower()=='steven':
            print('Intruder! All my homies hate intruders')
            break

    else:
        print('I do not recognize you. You are neither a friend nor a foe. My master will not like it if he finds you here.')
        break
