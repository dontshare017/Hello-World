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

    for turn in range(0,6):
        showBoard()
        if stepsLeft == 5:
            print('You have '+ str(stepsLeft)+ ' steps left, please enter your move.')
            print('Hint: Enter a number from 1-9 to place your move.')

        move = input()

        if board[str(move)] == ' ':
            board[str(move)] = player
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

        else:
            print('This space is already filled. Choose another destination')
            continue

        if stepsLeft <=3 :
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

            if stepsLeft == 1:
                print('Game over! Looks like no one won!')
                break

    print('A round is over. Do you want to play again? (Y/N)')
    playerChoice = input()
    if str(playerChoice) == 'Y':
        board = {'1': ' ', '2': ' ', '3': ' ',
                 '4': ' ', '5': ' ', '6': ' ',
                 '7': ' ', '8': ' ', '9': ' '}
        start()
    elif str(playerChoice) != 'N' or str(playerChoice) == 'Y':
        print('You did not enter a valid answer.')

if __name__ == "__main__":
    start()
