import random

print("Welcome to the Number Guessing Game!")

low = 1
high = 10

print("Think of a number between 1 to 10 and the computer will guess it.")

while low <= high:
    guess = random.randint(low, high)
    print("Computer's guess is:", guess)

    feedback = input("Is the guess too high (H), too low (L), or correct (C)? ").strip().upper()

    if feedback == 'C':
        print("Yay! The computer guessed your number correctly.")
        break
    elif feedback == 'H':
        high = guess - 1  # Reduce the upper bound
    elif feedback == 'L':
        low = guess + 1  # Increase the lower bound
    else:
        print("Invalid input. Please enter H, L, or C.")

    if low > high:
        print("The number is not in the range. Please restart the game.")
        break