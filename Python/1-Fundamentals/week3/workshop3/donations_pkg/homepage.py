# library to extract number from string
import re

# function to print out user interface


def show_homepage():
    print('         === DonateMe Homepage ===           ')
    print('-------------------------------------------- ')
    print('| 1.     Login       | 2.    Register       |')
    print('-------------------------------------------- ')
    print('| 3.     Donate      | 4.    Show Donations |')
    print('-------------------------------------------- ')
    print('|                5.    Exit                 |')
    print('-------------------------------------------- ')

# function to ask user to insert donation


def donate(username):
    # enter amount to donatea
    donation_amt = float(input('Enter amount to donate: '))

    donation = f'{username} donated ${donation_amt}'

    print('Thank you for your donation!')
    return donation

# function to show total donations


def show_donations(donations):
    print('\n--- All Donations ---')
    if not donations:
        print('Currently, there are no donations.')
    else:
        total = 0
        # print of donation values and get the total
        for item in donations:
            print(item)
            value_of_item = re.findall('\d+', item)
            total = total + float(value_of_item[0])
        print(f'Total = ${total}')
