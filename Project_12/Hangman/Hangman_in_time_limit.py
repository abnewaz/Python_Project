import random
from words import words
#from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly choose something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    # print(words)
    word = get_valid_word(words)
    print(word)
    word_letters = set(word)  # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    lives = 7

    # _______________getting user input ________________

    while len(word_letters) > 0 and lives > 0:
        # Letters used
        # ' '.join(['a', 'b', 'cd') --> 'a b cd'
        print('You have used these letters: ', ' '.join(used_letters))

        # what the current word is(ie W - R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        #print(lives_visual_dict[lives])
        print('current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1     # takes away a life if wrong
                print('\n Your letter, ', user_letter, ' is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Guess another letter. ')

        else:
            print('\n That is not a valid letter.')

       #  word_list = [letter if letter in used_letters else '_' for letter in word]
       #  print('current word: ', ' '.join(word_list))

       #gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        #print(lives_visual_dict[lives])
        print('You died, sorry. The word was ', word)
    else:
        print('Yay!! You guessed the word ', word, '!!')


if __name__ == '__main__':
    hangman()