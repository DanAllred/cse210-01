'''
Author: Dan Allred
Date 1/18/2022
'''
import sys
import random
from random import randint



die1 = 0
die2 = 0
die3 = 0
die4 = 0
die5 = 0

def main():
    
    def rolldie():
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        die3 = random.randint(1,6)
        die4 = random.randint(1,6)
        die5 = random.randint(1,6)
        print(f"You rolled: {die1} {die2} {die3} {die4} {die5}")

    def score():
        if die1 == 1:
            dice1 = 100
        if die2 == 1:
            dice2 = 100
        if die3 == 1:
            dice3 = 100
        if die4 == 1:
            dice4 = 100
        if die5 == 1:
            dice5 = 100
        if die1 == 5:
            dice1 = 50
        if die2 == 5:
            dice2 = 50
        if die3 == 5:
            dice3 = 50
        if die4 == 5:
            dice4 = 50
        if die5 == 5:
            dice5 = 50
        if die1 == 2 or 3 or 4 or 6:
            dice1 = 0
        if die2 == 2 or 3 or 4 or 6:
            dice2 = 0
        if die3 == 2 or 3 or 4 or 6:
            dice3 = 0
        if die4 == 2 or 3 or 4 or 6:
            dice4 = 0
        if die5 == 2 or 3 or 4 or 6:
            dice5 = 0
        total = int(dice1) + int(dice2) + int(dice3) + int(dice4) + int(dice5)
        print(f'You Scored: {total}')
        
        
        
        

    start = input('Roll dice? ')
    if start.lower() == 'y' or 'yes':
        rolldie()
        score()
        
    else:
        sys.exit


    print("")
    restart = input("Do want to roll Again?(y/n): ")
    if restart.lower() == "y":  
        main()
    else:
        sys.exit

if __name__ == "__main__":
    main()



