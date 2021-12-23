import random

high_score = 0


def dice_game():
    while True:
        global high_score
        print('Current High Score: ' + str(high_score))
        print('1) Roll Dice')
        print('2) Leave Game')

        choice = input('Enter your choice: ')

        if choice == '1':
            first_dice = random.randint(1, 6)
            second_dice = random.randint(1, 6)
            total s= first_dice + second_dice
            print('You have rolled a total of: ' + str(total))

            if total > high_score:
                high_score = total
                print('New high score!\n')

        if choice == '2':
            print('Goodbye!')
            break


dice_game()
