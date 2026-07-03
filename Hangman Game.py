import random

# List of predefined words
words = ["python", "apple", "computer", "school", "flower"]

# Randomly choose a word
word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses
attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Remaining Attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Correct Guess
    if guess in word:

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

        print("Correct Guess!")

    else:
        attempts -= 1
        print("Wrong Guess!")

# Result
if "_" not in guessed_word:
    print("\nCongratulations!")
    print("You guessed the word:", word)

else:
    print("\nGame Over!")
    print("The word was:", word)