import random

def get_random_word():
    word_list = ["apple", "banana", "cherry", "orange", "pear"]
    return random.choice(word_list)

def play_game():
    word = get_random_word()
    guesses = []
    max_attempts = 6
    attempts = 0

    while attempts < max_attempts:
        print("Guess the word:")
        for letter in word:
            if letter in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("\n")

        guess = input("Enter a letter: ").lower()
        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if guess in guesses:
            print("You have already guessed that letter.")
            continue

        guesses.append(guess)

        if guess not in word:
            attempts += 1
            print("Wrong guess. Attempts remaining:", max_attempts - attempts)
        
        if set(word) == set(guesses):
            print("Congratulations! You guessed the word:", word)
            break
    
    if attempts == max_attempts:
        print("Game over. The word was:", word)

play_game()