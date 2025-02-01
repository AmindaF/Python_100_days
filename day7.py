import random

word_list = ['Jazz', 'buzz', 'fizz', 'hangman']

def choose_word(word_list):
    return random.choice(word_list)

def display_hangman(tries):

    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def play_hangman():
    word = choose_word(word_list)
    word_length = len(word)
    guessed_word = ['_'] * word_length
    guessed_letters = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(' '.join(guessed_word))
    
    while tries > 0 and '_' in guessed_word:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            tries -= 1
            print(f"Wrong guess. You have {tries} tries left.")
        
        print(display_hangman(tries))
        print(' '.join(guessed_word))

    if '_' not in guessed_word:
        print("Congratulations! You've guessed the word correctly!")
    else:
        print(f"Game over! The word was: {word}")

play_hangman()