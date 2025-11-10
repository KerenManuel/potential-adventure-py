import random

try:

    while True:
        emoji_dictionary = {'r':'🪨', 'p':'📄', 's':'✂️'}
        choice = ('r','p','s')
        # Ask the user to make a choice
        user_choice = input("Make a choice, Rock, Paper, Scissors (r/p/s): ").lower()
        if user_choice != choice:
               print("Enter a valid choice")
            
        #print choices
        computer_choice = random.choice(choice)
        print(f'You chose {emoji_dictionary[user_choice]}')
        print(f'The computer chose {emoji_dictionary[computer_choice]}')

        #  Determine winner
        if user_choice == computer_choice:
            print("Tie")
        elif (
            (user_choice == 'r' and computer_choice == 's') or
            (user_choice == 's' and computer_choice == 'p') or
            (user_choice == 'p' and computer_choice == 'r') ):
              print("You won")
        else:
            print("You lose")

        # Ask the user if they want to continue(y/n)
        # If n type a message
        user_continue = input("Do you want to continue?(y/n): ").lower()
        if user_continue == 'n':
            print("Thank You")
            break

except KeyError:
        print()