# import the random module
import random

user_score = 0
computer_score = 0

# write 'hello world' to the console
print('Welcome to the game')

# create a function that returns a random option from the list scissors, paper, rock
def get_computer_choice():
    options = ['scissors', 'paper', 'rock']
    return random.choice(options)

# create a function to ask to to the user: "new game?", and read the input "y/n", validate the input, the function must return True if the user wants to play again, False otherwise
def new_game():    
    print('New game? y/n')
    answer = input()
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print('Invalid input')

# create a function that asks the user to choose between scissors, paper, rock, and returns the user's choice
def get_user_choice():
    print('Choose between scissors, paper, rock')
    choice = input()
    if choice in ['scissors', 'paper', 'rock']:
        return choice
    else:
        print('Invalid input')
        return get_user_choice()
    
# create a function that receives the user's choice and the computer's choice, and returns the result of the game
def get_result(user_choice, computer_choice):
    global user_score
    global computer_score
    if user_choice == computer_choice:
        return 'Draw'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return 'User wins'
    elif user_choice == 'paper' and computer_choice == 'rock':
        user_score += 1        
        return 'User wins'
    elif user_choice == 'rock' and computer_choice == 'scissors':
        user_score += 1
        return 'User wins'
    else:
        computer_score += 1
        return 'Computer wins'

# create a main loop function that will run the game
def main():
    global user_score
    global computer_score
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = get_result(user_choice, computer_choice)
        print(f'User choice: {user_choice}')
        print(f'Computer choice: {computer_choice}')
        print(f'Result: {result}')
        print(f'User score: {user_score}')
        print(f'Computer score: {computer_score}')
        if not new_game():
            break

# run the main loop function
main()

# write 'goodbye' to the console
print('Goodbye')