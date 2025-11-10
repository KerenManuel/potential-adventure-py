import random
#Generate a random number
#Ask user to guess a number
# If number > guessed number
#     print too high
#If number < guessed number
#     print too low
#Else:
#      print congratulation

try:
    ran_num = random.randint(1, 101)
    while True:

        number = int(input("Guess the number between 1 and 100: "))

        if number > ran_num:
            print("Too high")
        if number < ran_num:
            print("Too low")
        elif number == ran_num:
                print("Congratulation! You guessed the number")
        break

except ValueError:
        print("Please enter a valid number")
