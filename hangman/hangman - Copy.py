#Welcome to Krispy Kreme Hangman
#My name is Chase P
#How many dozens can i get for you today?

import os
import random
path = "puzzles"
data = "art"


def get_puzzle():
    file_names = os.listdir(path)

    for i, f in enumerate(file_names):
        print(str(i) + ".) " + f)

    choice = input("Pick an item: ")
    choice = int(choice)

    file = path + "/" + file_names[choice]
    print(file)

    with open(file, 'r') as f:
        lines = f.read().splitlines()

    print(lines)

    category_name = lines[0]
    puzzle = random.choice( lines[1:] )

    print(category_name)
    print(puzzle)

    return puzzle

def splash_screen():
   file2 = open('splash_screen')

    

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    while True:
        guess = input("Guess a letter: ")
        if guess.isalpha() == True and len(guess) ==1:
            return guess.lower()
        else:
            print("Type a single letter please!")

def display_board(solved, strikes, limit):
    print()
    print("################")
    print()
    print(solved + "            "" Strikes: " + str(strikes) +"/" + str(limit))
    print()
    print("################")

def show_result(solved, puzzle, limit, strikes):
    if solved == puzzle:
        print(" CONGRATS!!! YOU WINN " + name + "!!! WOOOOHOOO!")
    elif strikes == limit:
        print("AWWW DANGG!!! You suck! " + name + "! Try again next time!")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        if decision.lower() == 'y' or decision.lower() == 'yes':
            return True
        elif decision.lower() == 'n' or decision.lower() == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
def show_credits():
    print("""
########################################################################
#Thank you for playing this wonderful game made by Chase P    11/16/17 #
#If you have any ideas or recommendations that you'd like me to implant#
#Feel free to email cpolan9926@greenvilleschools.us                    #
########################################################################
""")
def play():
    limit = 10
    strikes = 0
    
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle,guesses)
    display_board(solved, strikes, limit)

    while solved != puzzle and strikes < limit:
        letter = get_guess()

        if letter not in puzzle:
            strikes += 1

        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved, strikes, limit)
    
    show_result(solved, puzzle, limit, strikes)
    
playing = True

splash_screen()
name = input("What shall I call you today? ")

while playing:
    play()
    playing = play_again()

show_credits()
