import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize variables
    attempts = 0
    user_guess = None

    print("Welcome to the Guessing Game!")

    while user_guess != secret_number:
        try:
            # Get user input for their guess
            user_guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            # Check if the guess is too high, too low, or correct
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()
