# importing module from banking package
from banking_pkg import account

# function to display the user account and choices to make


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
# Asking for user input
# Checking for the input string if it matches the requirement length
while True:
    name = input('Enter name to register: ')
    if(len(name) > 1 and len(name) <= 10):
        break
    elif(not name):
        print('You must enter a name.')
        continue
    print('The maximum name length is 10 characters.')

# Asking for user input
# Checking the input pin number if it matches the requirement length
while True:
    pin = input('Enter PIN: ')
    if(len(pin) == 4):
        break
    print('PIN must contain 4 numbers')

balance = 0
# display the user blaance and account name
print(f'{name} has been registered with a starting balance of ${balance}')

# conditional loop to validate the username and pin number
while True:
    print("          === Automated Teller Machine ===          ")
    print('LOGIN')
    name_to_validate = input('Enter name: ')
    pin_to_validate = input('Enter PIN: ')

    if(name_to_validate == name and pin_to_validate == pin):
        print('Login successful!')
        break
    print('Invalid credentials!')

# conditional loop to execute the function base the on choice user picks
while True:
    atm_menu(name)
    option = input('Choose an option: ')

    if(option == '1'):
        account.show_balance(balance)
    elif(option == '2'):
        balance = account.deposit(balance)
        print(f'Current Balance: ${balance:.2f}')
    elif(option == '3'):
        balance = account.withdraw(balance)
        print(f'Current Balance: ${balance:.2f}')
    elif(option == '4'):
        account.logout(name)
        break
