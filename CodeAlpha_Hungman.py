import random

# 1. Predefined word list
words = ["python", "jupiter", "keyboard", "coding", "pixel"]
secret_word = random.choice(words)

# Initialize game state
guessed_letters = []
incorrect_guesses = 0
max_lives = 6

print("--- Welcome to Hangman! ---")

# 2 & 3. Main Game Loop
while incorrect_guesses < max_lives:
    # Display the current progress (e.g., "p _ t h _ n")
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print(f"\nWord: {display_word}")
    print(f"Lives remaining: {max_lives - incorrect_guesses}")
    print(f"Guessed so far: {', '.join(guessed_letters)}")

    # Check if the player has won
    if "_" not in display_word:
        print("Congratulations! You guessed the word!")
        break

    # Get player input
    guess = input("Guess a letter: ").lower()

    # Validation & Logic
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print(f"Good job! '{guess}' is in the word.")
    else:
        incorrect_guesses += 1
        print(f"Sorry, '{guess}' is not there.")

# End of game check
if incorrect_guesses == max_lives:
    print("\nGAME OVER!")
    print(f"The word was: {secret_word}")