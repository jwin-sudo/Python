# function to display balance
def show_balance(balance):
    print(f'Current Balance: ${balance:.2f}')

# function to make a deposit


def deposit(balance):
    amount = input('Enter amount to deposit: ')
    return balance + float(amount)

# function to make a withdrawal


def withdraw(balance):
    amount = input('Enter amount to withdraw: ')
    # checking the balance if there's any money
    if(balance > 0):
        return balance - float(amount)
    else:
        print('Where are you going to get that kind of money')
        return balance

# function to logout the user once done


def logout(name):
    print(f'Goodbye {name}!')
