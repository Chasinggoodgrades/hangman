#Welcome to Krispy Kreme Hangman
#My name is Chase P
#How many dozens can i get for you today?

def get_puzzle():
    return "krispykreme"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    letter = input("Guess a letter: ")
    return letter

def display_board(solved):
    print()
    print("################")
    print()
    print(solved)
    print()
    print("################")
def show_result():
    print("You win!")
    
def play():
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle,guesses)
    display_board(solved)

    while solved != puzzle:
        guesses += get_guess()
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result()
    
    
play()
