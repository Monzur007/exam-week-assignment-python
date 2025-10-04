import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.\n")

    target = random.randint(1, 100)
    attempts = 0

    while True:
        guess_input = input("Enter your guess: ")

        try:
            guess = int(guess_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer between 1 and 100.\n")
            continue

        if guess < 1 or guess > 100:
            print("Out of bounds. Please enter a number between 1 and 100.\n")
            continue

        attempts += 1

        if guess < target:
            print("Too low!\n")
        elif guess > target:
            print("Too high!\n")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
