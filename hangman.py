import random
import string

import graphics

graphic = graphics.graphic


def set_dificult_level():
    dificult_level_dict = {
        1: 'easy',
        2: 'medium',
        3: 'hard'
    }
    while True:
        dificult_level = input(f"Choose dificult level {dificult_level_dict}\n")

        if dificult_level.isdigit() and int(dificult_level) in dificult_level_dict.keys():
            dificult_level_int = int(dificult_level)
            print(f'you chose level {dificult_level_dict[dificult_level_int]}')
            return dificult_level_int
            print('choose right value')


def word_choose():
    with open('countries-and-capitals.txt', 'r') as file:
        words = file.read()
    countries = []
    capitals = []
    words_lines = words.split('\n')

    for i in words_lines:
        pair_of_words = i.split(' | ')

        countries.append(pair_of_words[0])
        capitals.append(pair_of_words[1])

    words_list = countries + capitals
    return random.choice(words_list)


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
            if letter == 'quit':
                print('you quit the game')
                exit()
            if letter == '' or len(letter) > 1 or letter.isdigit():
                print('give a letter')
                continue
            #  string.ascii_letters
            elif letter in list_of_word_lower and letter not in already_tried_letters:
                for index in range(len(hiden_word)):
                    if list_of_word_lower[index] == letter:
                        hiden_word[index] = list_of_word[index]

            elif letter not in already_tried_letters:
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


while True:
    word_to_guess = word_choose()
    dificulty = set_dificult_level()
    hangmen(dificulty, word_to_guess)
