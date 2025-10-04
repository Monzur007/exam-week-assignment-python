
# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Cannot perform modulus by zero."
    return x % y

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please enter a number from 1 to 5.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(f"{num1} / {num2} = {result:.2f}")
    elif choice == '5':
        result = modulus(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(f"{num1} % {num2} = {result}")

if __name__ == "__main__":
    main()

    #--------------
    # Number guessing game

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