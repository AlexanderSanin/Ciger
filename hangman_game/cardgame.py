# Author : Romijul Laskar
# Copyrights: 2022 all rights reserved

# Title :- The PREDICT-The-WORD game using python

# importing all the required libraries
from words import Word

print('This is the PREDICT-The-WORD game. You have got 7 chances to guess the word.')
print('BEST OF LUCK!!.. Enjoy the game..')

HANGMAN = (
    """
    x-------x
    """,
    """
    x-------x
    |
    |
    |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    GAME OVER
    """
)

MAX_ATTEMPTS = len(HANGMAN) - 1
WORD_TO_GUESS = Word()
HIDDEN_WORD = ['_'] * len(WORD_TO_GUESS)
LETTERS_GUESSED = []

def display_hidden_word():
    print(' '.join(HIDDEN_WORD))

def update_hidden_word(letter):
    for index, char in enumerate(WORD_TO_GUESS):
        if char == letter:
            HIDDEN_WORD[index] = letter

def is_word_guessed():
    return '_' not in HIDDEN_WORD

def start_game():
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        display_hidden_word()
        user_guess = input('Guess a letter: ').lower()

        if user_guess in LETTERS_GUESSED:
            print('You already guessed it.. PLEASE PAY ATTENTION!')
            continue

        LETTERS_GUESSED.append(user_guess)

        if user_guess in WORD_TO_GUESS:
            print("Going well!.. It's in the word....Excellent work!")
            update_hidden_word(user_guess)

            if is_word_guessed():
                print('--------------BRILLIANT YOU WIN..!-------------')
                print('************** Congratulations ****************')
                break
        else:
            print(f"{user_guess}.. You have tried the BEST but.. Not in my word..")
            attempts += 1
            print(HANGMAN[attempts])

    if attempts == MAX_ATTEMPTS:
        print('GAME OVER. The word was:', WORD_TO_GUESS)

# starting the game
start_game()
