import random
import time

# A dictionary of categories and corresponding words for the hangman game.
# Players choose a category, and a random word is selected.
categories = {
    'Animals': ['elephant', 'tiger', 'kangaroo'],
    'Fruits': ['apple', 'banana', 'cherry'],
    'Countries': ['india', 'france', 'brazil'],
    'Movies': ['inception', 'gladiator', 'matrix']
}

# Visual representations of the hangman at different stages of the game.
# The number of incorrect guesses determines which image is shown.
hangman_images = [
    '''
      ------
      |    |
           |
           |
           |
           |
     =======
    ''',
    '''
      ------
      |    |
      O    |
           |
           |
           |
     =======
    ''',
    '''
      ------
      |    |
      O    |
      |    |
           |
           |
     =======
    ''',
    '''
      ------
      |    |
      O    |
     /|    |
           |
           |
     =======
    ''',
    '''
      ------
      |    |
      O    |
     /|\\   |
           |
           |
     =======
    ''',
    '''
      ------
      |    |
      O    |
     /|\\   |
     /     |
           |
     =======
    ''',
    '''
      ------
      |    |
      O    |
     /|\\   |
     / \\   |
     =======
    '''
]

# This function provides a simple hint by returning the first letter of the word.
def give_hint(word):
    return f"The word starts with: {word[0]}"

# This function ensures the player provides a valid input (a single letter that hasn't been guessed yet).
def get_valid_input(guessed_letters, incorrect_guesses):
    while True:
        guess = input("Guess a letter: ").lower()  # Input is converted to lowercase for consistency.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")  # Ensures the input is a single alphabet character.
        elif guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter!")  # Prevents duplicate guesses.
        else:
            return guess  # Returns the valid input.

# This function allows the player to choose the difficulty level (Easy, Medium, Hard).
def set_difficulty():
    while True:
        difficulty = input("Choose difficulty (Easy/Medium/Hard): ").lower()
        if difficulty == 'easy':
            return 8  # Easy: 8 incorrect guesses allowed.
        elif difficulty == 'medium':
            return 6  # Medium: 6 incorrect guesses allowed.
        elif difficulty == 'hard':
            return 4  # Hard: 4 incorrect guesses allowed.
        else:
            print("Invalid choice. Please choose again.")  # Prompts the user until they enter a valid choice.

# Core function of the hangman game.
def hangman_game():
    print("Choose a category:")
    for category in categories:
        print(category)  # Displays all available categories.

    # Ensures the player selects a valid category.
    while True:
        category = input("Enter category: ").capitalize()
        if category in categories:
            break
        print(f"Invalid category. Please choose from: {', '.join(categories.keys())}")

    # Randomly selects a word from the chosen category.
    word = random.choice(categories[category])
    word_length = len(word)
    guesses_left = set_difficulty()  # Sets the number of allowed guesses based on difficulty.
    guessed_letters = []  # List to keep track of correct guesses.
    incorrect_guesses = []  # List to keep track of incorrect guesses.
    display = ['_'] * word_length  # Represents the word as blanks initially.

    start_time = time.time()  # Tracks the start time of the game.
    time_limit = 30  # Sets a time limit of 30 seconds for the game.
    hint_used = False  # Tracks whether the hint has been used.

    # Asks the player if they want a hint.
    if not hint_used and input("Want a hint? (yes/no): ").lower() == "yes":
        print(give_hint(word))
        hint_used = True

    # Main game loop: continues until the player runs out of guesses or successfully guesses the word.
    while guesses_left > 0 and '_' in display:
        print(f"\nWord: {' '.join(display)}")  # Displays the current state of the word.
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")  # Shows incorrect guesses.
        print(f"Guesses left: {guesses_left}")  # Shows remaining guesses.
        print(f"Time left: {max(0, time_limit - int(time.time() - start_time))} seconds")  # Shows remaining time.

        # Ends the game if the time limit is exceeded.
        if time.time() - start_time > time_limit:
            print("Time's up! You lose.")
            break

        print(hangman_images[len(incorrect_guesses)])  # Displays the appropriate hangman image.
        guess = get_valid_input(guessed_letters, incorrect_guesses)  # Gets a valid input from the player.

        # If the guess is correct, update the display with the guessed letter.
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            guessed_letters.append(guess)
            display = [guess if word[i] == guess else display[i] for i in range(len(word))]
        else:
            # If the guess is incorrect, decrement guesses and update incorrect guesses list.
            print(f"Oops! The letter '{guess}' is not in the word.")
            incorrect_guesses.append(guess)
            guesses_left -= 1

    # Checks if the player has successfully guessed the word.
    if '_' not in display:
        print(f"Congratulations! You've guessed the word: {word}")
        return True, guesses_left
    else:
        print(f"Game Over! The word was: {word}")
        return False, 0

# Function to manage multiple rounds of the game and track statistics.
def play_hangman():
    total_games = 0  # Tracks the total number of games played.
    games_won = 0  # Tracks the number of games won.
    high_score = float('inf')  # Tracks the best score (fewest incorrect guesses).

    while True:
        print("\nStarting a new game...")
        won, guesses_left = hangman_game()  # Plays a single round of the game.

        total_games += 1
        if won:
            games_won += 1
            high_score = min(high_score, guesses_left)  # Updates high score if the current game is better.

        # Displays game statistics.
        print(f"\nTotal Games Played: {total_games}")
        print(f"Games Won: {games_won}")
        print(f"High Score (Fewest guesses left): {high_score}")

        # Asks the player if they want to play again.
        if input("\nDo you want to play again? (yes/no): ").lower() != 'yes':
            break

# Runs the game if the script is executed directly.
if __name__ == "__main__":
    play_hangman()