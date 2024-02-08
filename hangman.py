import random
import graphics

graphic = graphics.graphic
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
        words = file.read()
    countries = []
    capitals = []
    words2 = words.split('\n')
    words2.pop()
    for i in words2:
        pair_of_words = i.split(' | ')

        countries.append(pair_of_words[0])
        capitals.append(pair_of_words[1])

    words = countries + capitals
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
            if letter == 'quit':
                print('you quit the game')
                exit()
            if letter == '' or len(letter) > 1:
                print('give me a letter')
                continue
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


while True:
    word_to_guess = word_choose()
    dificulty = set_dificult_level()
    hangmen(dificulty, word_to_guess)
