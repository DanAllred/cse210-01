'''
W02 Prove: Developer - Solo Code Submission (Tic-Tac-Toe)
Author: Daniel Allred
Date: 1/12/2022
'''

#Tic-Tac-Toe game#

import sys
import time

def print_pause3(message):
    print(message)
    time.sleep(3)

def print_pause2(message):
    print(message)
    time.sleep(2)

def print_pause1(message):
    print(message)
    time.sleep(1)

#War Games easter egg, Yes I am that old. Have to get quote exact otherwise TicTacToe just starts... or player said no!#
playgame = input('SHALL WE PLAY A GAME? ')
if playgame.lower() == 'love to. how about global thermonuclear war?':
    print('')
    print("Wouldn't you prefer a good game of Tic-Tac-Toe?")
    print('')
    gtw = input('')
    if gtw.lower() == "later. let's play global thermonuclear war.":
        print('')
        print("FINE.")
        print_pause3('')
        print("Just kidding, lets play Tic-Tac-To:")
        print_pause2('')
elif playgame.lower() in('n', 'no'):
    sys.exit()

the_board = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in the_board:
    board_keys.append(key)

def printBoard(board):
    print('')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def main():

    turn = 'X'
    count = 0



    for i in range(10):
        print('')
        print(turn + "'s turn. Choose a number (1-9): ")
        printBoard(the_board)
        print('')
        move = input()      
        if the_board[move] == ' ':
            print('............')
            the_board[move] = turn
            count += 1
        else:
            print('')
            print("Spot already in play.")
            print('')
            continue



        if count >= 5:
            if the_board['1'] == the_board['2'] == the_board['3'] != ' ': 
                printBoard(the_board)
                print('')
                print("Game Over")
                print('')                
                print(turn + " won!")                
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ': 
                printBoard(the_board)
                print('')
                print("Game Over")
                print('')                
                print(turn + " won!")
                break
            elif the_board['7'] == the_board['8'] == the_board['9'] != ' ': 
                printBoard(the_board)
                print('')
                print("Game Over")
                print('')                
                print(turn + " won!")
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ': 
                printBoard(the_board)
                print('')
                print("Game Over")
                print('')                
                print(turn + " won!")
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
                printBoard(the_board)
                print('')
                print("Game Over")
                print('')                
                print(turn + " won!")
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ': 
                printBoard(the_board)
                print('')
                print("Game Over")
                print('')                
                print(turn + " won!")
                break 
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ': 
                printBoard(the_board)
                print('')
                print("Game Over")
                print('')                
                print(turn + " won!")
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ': 
                printBoard(the_board)
                print('')
                print("Game Over")
                print('')                
                print(turn + " won!")
                break 



        if count == 9:
                print('')
                print("Tie game!")
                print('')                
                restart = input("Do want to play Again?(y/n): ")
                if restart.lower() == "y":  
                    for key in board_keys:
                        the_board[key] = " "
                    main()
                else:
                    print('')
                    print('Game will now exit')
                    print_pause1('')
                    sys.exit()


        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        


    print("")
    restart = input("Do want to play Again?(y/n): ")
    if restart.lower() == "y":  
        for key in board_keys:
            the_board[key] = " "
        main()



if __name__ == "__main__":
    main()



'''
Part Two:
How did you use a version control system to develop the programs? 

I use Github to manage version control. I rarely go on Github as I am the only person using the file
and am using only one device to edit the file. If I were to use other devices I would probably
use github desktop and manage the most current file by opening the reposiory on visual code and then
commiting when done. In reality though I rarely push changes until I am done testing. Otherwise I 
end up with 50 changes of something small like a spelling error fix. So I try and minimize amounts of
commits and pushes.
'''