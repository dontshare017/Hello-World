board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

def showBoard():
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'] )
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')

def start():
    player = 'X'
    CPU = 'O'
    stepsLeft = 5
    import random
    import os

    for turn in range(0,6):
        showBoard()
        if stepsLeft == 5:
            print('You have '+ str(stepsLeft)+ ' steps left, please enter your move.')
            print('Hint: Enter a number from 1-9 to place your move.')

        move = input()

        if board[str(move)] == ' ':
            board[str(move)] = player
            if stepsLeft == 1:
                stepsLeft -=1
                break
            else:
                stepsLeft -= 1
                print("You have " + str(stepsLeft) + " steps left. Please choose your move")


            CPUMove = random.randint(1,9)
            if board[str(CPUMove)] == ' ':
                board[str(CPUMove)] = CPU
            else:
                CPUMove = random.randint(1,9)
                while board[str(CPUMove)] != ' ':
                    CPUMove = random.randint(1,9)
                else:
                    board[str(CPUMove)] = CPU

        elif board[str(move)] != ' ':
            print('This space is already filled. Choose another destination')
            continue

        if stepsLeft <=2:
            if board['1'] == board['2'] == board ['3'] != ' ' or board['1'] == board['4'] == board ['7'] != ' ' or board['1'] == board['5'] == board ['9'] != ' ':
                showBoard()
                if board['1'] == player:
                    print('Congratulation! You have won!')
                else:
                    print('Oh no. You lost to the CPU :(')
                break

            elif board['2'] == board['5'] == board ['8'] != ' ':
                showBoard()
                if board['2'] == player:
                    print('Congratulation! You have won!')
                else:
                    print('Oh no. You lost to the CPU :(')
                break

            elif board['3'] == board['6'] == board ['9'] != ' ' or board['3'] == board['5'] == board ['7'] != ' ':
                showBoard()
                if board['3'] == player:
                    print('Congratulation! You have won!')
                else:
                    print('Oh no. You lost to the CPU :(')
                break

            elif board['4'] == board['5'] == board ['6'] != ' ':
                showBoard()
                if board['4'] == player:
                    print('Congratulation! You have won!')
                else:
                    print('Oh no. You lost to the CPU :(')
                break

            elif board['7'] == board['8'] == board ['9'] != ' ':
                showBoard()
                if board['7'] == player:
                    print('Congratulation! You have won!')
                else:
                    print('Oh no. You lost to the CPU :(')
                break
            else:
                if stepsLeft == 0:
                    print('Game over! Looks like no one won!')

    if stepsLeft == 0:
        if board['1'] == board['2'] == board ['3'] != ' ' or board['1'] == board['4'] == board ['7'] != ' ' or board['1'] == board['5'] == board ['9'] != ' ':
            showBoard()
            if board['1'] == player:
                print('Congratulation! You have won!')
            else:
                print('Oh no. You lost to the CPU :(')

        elif board['2'] == board['5'] == board ['8'] != ' ':
            showBoard()
            if board['2'] == player:
                print('Congratulation! You have won!')
            else:
                print('Oh no. You lost to the CPU :(')

        elif board['3'] == board['6'] == board ['9'] != ' ' or board['3'] == board['5'] == board ['7'] != ' ':
            showBoard()
            if board['3'] == player:
                print('Congratulation! You have won!')
            else:
                print('Oh no. You lost to the CPU :(')

        elif board['4'] == board['5'] == board ['6'] != ' ':
            showBoard()
            if board['4'] == player:
                print('Congratulation! You have won!')
            else:
                print('Oh no. You lost to the CPU :(')

        elif board['7'] == board['8'] == board ['9'] != ' ':
            showBoard()
            if board['7'] == player:
                print('Congratulation! You have won!')
            else:
                print('Oh no. You lost to the CPU :(')
        else:
            print('Game over! Looks like no one won!')


start()

print('A round is over. Do you want to play again? (Y/N)')
playerChoice = input()
if str(playerChoice) == 'Y':
    board = {'1': ' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '7': ' ', '8': ' ', '9': ' '}
    start()

elif str(playerChoice) == 'N':
    print('Alrighty! Have a good day!')
    input(' ')
elif str(playerChoice) != 'N' and str(playerChoice) != 'Y':
    while str(playerChoice) != 'N' and str(playerChoice) != 'Y':
        print('You did not enter a valid answer.')
        playerChoice = input()
        if str(playerChoice) == 'Y':
            board = {'1': ' ', '2': ' ', '3': ' ',
                     '4': ' ', '5': ' ', '6': ' ',
                     '7': ' ', '8': ' ', '9': ' '}
            start()
            os.system('pause')
        elif str(playerChoice) == 'N':
            input('Sad to see you go :(, how about you!?')
            print('Alrighty! Have a good day!')
