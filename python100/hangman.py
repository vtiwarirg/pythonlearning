import random
print("Welcome to the Hangman game!")
print("Generating a random word...")
print("Generate blank spaces for the word...")
print("Ask the user to guess a letter...")
print("Check if the letter is in the word...")
print("If the letter is in the word, replace the blank space with the letter...")
print("If the letter is not in the word, loose a life...")
print("Check if the user has guessed the word or if they have run out of guesses...")
print("If the user has guessed the word, congratulate them...")

lives = 6

chosen_word = random.choice(["python", "hangman", "programming", "developer", "challenge"])
print(f"The chosen word is: {chosen_word}")
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
    
print(f"The word to guess: {placeholder}")

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_letters:
        print(f"You have already guessed the letter '{guess}'. Try again.")
        continue
    
    correct_letters.append(guess)
    
    if guess in chosen_word:
        print(f"Good job! The letter '{guess}' is in the word.")
        placeholder = "".join([chosen_word[i] if chosen_word[i] == guess else placeholder[i] for i in range(word_length)])
    else:
        lives -= 1
        print(f"Sorry, the letter '{guess}' is not in the word. You have {lives} lives left.")
    
    print(f"Current word: {placeholder}")
    
    if "_" not in placeholder:
        print("Congratulations! You've guessed the word!")
        game_over = True
    elif lives == 0:
        print(f"You've run out of lives. The word was '{chosen_word}'. Better luck next time!")
        game_over = True




