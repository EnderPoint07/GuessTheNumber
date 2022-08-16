# Game which gives the player 3 chances to guess a random number between 0 and 100.

# Imports
import random


# Main function
def main():
    # Variables
    correct_number = 0
    user_guess = 0
    chances = 3

    # Make a random number between 0 and 10
    correct_number = random.randint(1, 10)

    while chances != 0:  # Loop until chances are over

        # Get user's guess
        user_guess = input(
            "Enter a number between 0 and 10. You have " + str(chances) + " chances to guess the correct number\n")

        # Check if user is correct
        if int(user_guess) == correct_number:
            # See if the user wants to play again
            play_again = input("You have guessed correctly! Do you want to play again? (y/n)\n")
            if play_again == "y":
                main()
            elif play_again == "n":
                return
        else:  # If the user is wrong then subtract one from the chances
            print("Wrong number! Try again")
            chances -= 1
    # Loop ends if chances are over

    # Ask the user to play again
    play_again = input(
        "You ran out of guesses. The correct number was " + '\033[1m' + str(correct_number) + '\033[0m'
        + " Do want to try again? (y/n)\n")
    if play_again == "y":
        main()
    elif play_again == "n":
        return


# Call the main function
main()
