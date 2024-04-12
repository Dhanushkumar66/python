import random

def get_player_choice():
    
    while True:
        player_choice = input("Enter your choice ~ 'stone', 'paper', or 'scissor': ").strip().lower()
        if player_choice in ['stone', 'paper', 'scissor']:
            return player_choice
            
            
def get_computer_choice():
    
    return random.choice(['stone', 'paper', 'scissor'])

def determine_winner(player_choice, computer_choice):

    if player_choice == computer_choice:
        return "It's draw"

    if (player_choice == 'stone' and computer_choice == 'scissor') or \
       (player_choice == 'paper' and computer_choice == 'stone') or \
       (player_choice == 'scissor' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def start_game():
    print("game of stone,paper,scissor")
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(player_choice, computer_choice))

        start_again = input("try again (yes/no): ").strip().lower()
        if start_again != 'yes':
            print("thank you")
            break
start_game()
