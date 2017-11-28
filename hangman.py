#Hangman
#Justin Hatley

def start_screen():
    print("""
 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌          ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░▌ ▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌▐░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌▐░▌ ▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌
 ▀         ▀  ▀         ▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀        ▀▀ 
    """)
    
def show_credits():
    print()
    print("""
███╗   ███╗ █████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗         ██╗██╗   ██╗███████╗████████╗██╗███╗   ██╗    ██╗  ██╗ █████╗ ████████╗██╗     ███████╗██╗   ██╗
████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝         ██║██║   ██║██╔════╝╚══██╔══╝██║████╗  ██║    ██║  ██║██╔══██╗╚══██╔══╝██║     ██╔════╝╚██╗ ██╔╝
██╔████╔██║███████║██║  ██║█████╗      ██████╔╝ ╚████╔╝          ██║██║   ██║███████╗   ██║   ██║██╔██╗ ██║    ███████║███████║   ██║   ██║     █████╗   ╚████╔╝ 
██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██╗  ╚██╔╝      ██   ██║██║   ██║╚════██║   ██║   ██║██║╚██╗██║    ██╔══██║██╔══██║   ██║   ██║     ██╔══╝    ╚██╔╝  
██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██████╔╝   ██║       ╚█████╔╝╚██████╔╝███████║   ██║   ██║██║ ╚████║    ██║  ██║██║  ██║   ██║   ███████╗███████╗   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═════╝    ╚═╝        ╚════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝   ╚═╝                                                                                                                                                               
    """)
    
def get_puzzle():
    return "yessir"

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
        letter = input("Guess a letter: ")

        if len(letter) == 1:
            if(letter).isalpha():
                return letter
            else:
                print("Enter one letter at a time.")
        else:
                print("Enter one letter at a time.")    

def display_board(solved):
    print(solved)

def show_result(result):
    if result == 0:
         print("Congratulations!")
    else:
        print("Loser.")
    

def play_again(name):
    while True:
        decision = input("Do you wanna play again " + name + " ? (y/n)")
        print()
        decision = decision.lower()

        if decision == "y" or decision == "yes":
            return True
        elif decision == "n" or decision == "no":
            print("Goodbye!")
            return False
        
        else:
            print("Please enter a valid answer.")
    
def play(name):
    print("Welcome to Hangman Game, " + name + "!!")
    print("I will give you 5 guesses to guess the word.")
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved)

    strikes = 0
    limit = 5
    result = 0
    print(solved)
    gameover = 0

    while solved != puzzle and gameover == 0:
        letter = get_guess()

        if letter not in puzzle:
            strikes +=1
            print("That letter isn't in the word!")
            print("You have " + str(strikes) + " strikes. Try not to lose " + name + " .")
            print()
            if strikes == limit:
                print("You lost " + name + ", that word was easy too!")
                result = 1
                gameover = 1
        
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result(result)

start_screen()
playing = True

while playing:
    name = input("What is your name?")
    play(name)
    playing = play_again(name)
show_credits()
