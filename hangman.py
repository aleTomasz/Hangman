# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
import csv
import random

difficulty = "1"  # sample data, normally the user should choose the difficulty

# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
word_to_guess = "Cairo"  # sample data, normally the word should be chosen from the countries-and-capitals.txt
lives = 5  # sample data, normally the lives should be chosen based on the difficulty

# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"


# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions


# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
already_tried_letters = []  # this list will contain all the tried letters

# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".


# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.


# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4
graphic = [
    """
           +---------------+
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
        =======================
    """,
    """
           +---------------+
           |               |
           |               O
           |
           |
           |
           |
           |
           |
           |
           |
        =======================
    """,
    """
           +---------------+
           |               |
           |               O
           |               |
           |
           |
           |
           |
           |
           |
           |
        =======================
    """,
    """
           +---------------+
           |               |
           |               O
           |             --|
           |
           |
           |
           |
           |
           |
           |
        =======================
    """,
    """
           +---------------+
           |               |
           |               O
           |             --|--
           |
           |
           |
           |
           |
           |
           |
        =======================
    """,
    """
           +---------------+
           |               |
           |               O
           |             --|--
           |              |
           |
           |
           |
           |
           |
           |
        =======================
    """,
    """
           +---------------+
           |               |
           |               O
           |             --|--
           |              | |
           |                   
           |
           |
           |
           |
           |
        =======================
    """,
]
dificult_level_dict = {
    1: 'easy',
    2: 'medium',
    3: 'hard'
}


def set_dificult_level():
    dificult_level_int = 0
    while True:
        dificult_level = input(f"Choose dificult level {dificult_level_dict}\n")
        if dificult_level.isdigit():
            dificult_level_int = int(dificult_level)
        if dificult_level_int in dificult_level_dict.keys():
            print(f'you chose level {dificult_level_dict[dificult_level_int]}')
            return dificult_level_int
        else:
            print('choose right value')


def word_choose():


    with open('countries-and-capitals.txt', 'r') as file:
      words=file.read()
    countries=[]
    capitals=[]
    words2=words.split('\n')
    words2.pop()
    for i in words2:
        pair_of_words=i.split(' | ')

        countries.append(pair_of_words[0])
        capitals.append(pair_of_words[1])

    words=countries+capitals
    return random.choice(words)








def hide_word(word_to_guess):
    hidden_word_list = list(word_to_guess)
    for index in range(len(hidden_word_list)):
        if hidden_word_list[index] != " ":
            hidden_word_list[index] = "_"
    return hidden_word_list


def hangmen(dificult_level, word_to_guess):
    list_of_word = list(word_to_guess)
    list_of_word_lower = list(word_to_guess.lower())
    hiden_word = hide_word(word_to_guess)
    already_tried_letters = []
    lives = 7
    already_lives = 0

    while True:

        if "_" in hiden_word:
            print(''.join(hiden_word))
            letter = input('Give letter: ').lower()
            if letter==''or len(letter)>1:
                continue
            if (letter == 'quit'):
                print('you quit the game')
                break
            elif letter in list_of_word_lower and not letter in already_tried_letters:
                for index in range(len(hiden_word)):
                    if list_of_word_lower[index] == letter:
                        hiden_word[index] = list_of_word[index]

            elif not letter in already_tried_letters:
                print('you lost live\n')
                print(graphic[already_lives])
                already_lives += dificult_level
                if already_lives >= lives:
                    print('GAME OVER')
                    break
            already_tried_letters.append(letter)
        else:
            print(''.join(hiden_word))
            print('YOU WIN!!!')
            break


word_to_guess = word_choose()
dificulty = set_dificult_level()
hangmen(dificulty, word_to_guess)
