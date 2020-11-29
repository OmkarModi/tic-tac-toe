board={'7': ' ' , '8': ' ' , '9': ' ' ,
        '4': ' ' , '5': ' ' , '6': ' ' ,
        '1': ' ' , '2': ' ' , '3': ' ' }

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():

    turn = 'X'
    count=0

    while count <= 9 :
        printBoard(board)
        print("it your turn"+turn+"which place to play?")
        move=input()

        if board[move]==' ':
            board[move]=turn
            count += 1

        else:
            print("place is already filled please select empty place")
            continue

        if count>=5:
             if board['7'] == board['8'] == board['9'] != ' ': # across the top
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
             elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
             elif board['1'] == board['2'] == board['3'] != ' ': # across the bottom
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
             elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
             elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
             elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
             elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
             elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        if turn=='X':
            turn='O'
        else:
            turn='X'

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board.keys():
            board[key] = " "

        game()

game()
