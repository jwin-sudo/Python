from module import homepage, clues


def app():
    homepage.homepage()
    word_dict = {"dog": 100, "cat": 200,
                 "zebra": 300, "dinosaur": 400, "lion": 500}

    alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                     "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    choice = int(input('Please select your prize choice: '))
    total = 0
    guess = 5
    word_arr = []
    guess_arr = []
    guess_str = ''

    if choice in word_dict.values():
        for key, value in word_dict.items():
            if choice == value:
                word_arr.append(key)
        word_str = ''.join(word_arr)

        list_word_str = list(word_str)

    print(f'The word has {len(word_str)} blank')
    print("_ " * len(word_str))

    clues.hangman_clues(choice)

    print(f'You have {guess} guesses\n')

    while True:
        user_guess = input('Please make a guess:')
        if user_guess in alphabet_list and user_guess in list_word_str:
            guess_arr.append(user_guess)
            print(
                f'{strings_validation(guess_arr, list_word_str, guess,total,choice)}\n')
            homepage.hangman(guess)
        else:
            guess = guess - 1

            if(guess == 4):
                print(
                    f'{strings_validation(guess_arr, list_word_str, guess,total,choice)}\n')
                homepage.hangman(guess)
                continue

            elif(guess == 3):
                print(
                    f'{strings_validation(guess_arr, list_word_str, guess,total,choice)}\n')
                homepage.hangman(guess)
                continue

            elif(guess == 2):
                print(
                    f'{strings_validation(guess_arr, list_word_str, guess,total,choice)}\n')
                homepage.hangman(guess)
                continue

            elif(guess == 1):
                print(
                    f'{strings_validation(guess_arr, list_word_str, guess,total,choice)}\n')
                homepage.hangman(guess)
                continue

            elif(guess == 0):
                homepage.hangman(guess)
                print(
                    f'{strings_validation(guess_arr, list_word_str, guess,total,choice)}\n')
                break


def strings_validation(guess_arr, list_word_str, guess_left, total_pt, user_choice):
    if guess_left == 5:
        if guess_arr != list_word_str:
            print(f'You have {guess_left} strikes left.')
            return 'Keep guessing!'

        else:
            print('You have guessed the word correctly!\n')
            print('It is a', ''.join(list_word_str) + '!')
            print(f'You have {total_pt+user_choice} points')
            quit()

    elif guess_left == 4:
        if guess_arr != list_word_str:
            print(f'You have {guess_left} strikes left.')
            return 'Keep guessing!'

        else:
            print('You have guessed the word correctly!\n')
            print('It is a', ''.join(list_word_str) + '!')
            print(f'You have {total_pt+user_choice} points')
            quit()

    elif guess_left == 3:
        if guess_arr != list_word_str:
            print(f'You have {guess_left} strikes left.')
            return 'Keep guessing!'

        else:
            print('You have guessed the word correctly!\n')
            print('It is a', ''.join(list_word_str) + '!')
            print(f'You have {total_pt+user_choice} points')
            quit()

    elif guess_left == 2:
        if guess_arr != list_word_str:
            print(f'You have {guess_left} strikes left.')
            return 'Keep guessing!'

        else:
            print('You have guessed the word correctly!\n')
            print('It is a', ''.join(list_word_str) + '!')
            print(f'You have {total_pt+user_choice} points')
            quit()

    elif guess_left == 1:
        if guess_arr != list_word_str:
            print(f'You have {guess_left} strikes left.')
            return 'Keep guessing!'

        else:
            print('You have guessed the word correctly!\n')
            print('It is a', ''.join(list_word_str) + '!')
            print(f'You have {total_pt+user_choice} points')
            quit()

    elif guess_left == 0:
        print('Game Over. You ran out your guesses.')
        print(f'You have {total_pt} point.')
        quit()


app()
