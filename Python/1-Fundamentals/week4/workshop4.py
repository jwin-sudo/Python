# user class to store name, pin and password
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    # method to change user name
    def change_name(self, new_name):
        if new_name < 2 or new_name > 10:
            return None
        else:
            self.name = new_name

    # method to change user pin
    def change_pin(self, new_pin):
        if new_pin < 4 or new_pin > 4:
            return None
        else:
            self.pin = new_pin

    # method to change user password
    def change_password(self, new_password):
        if new_password < 5:
            return None
        else:
            self.password = new_password


""" Driver Code for Task 1
user = User("Bob", 1234, "password")
print(user.name, user.pin, user.password) """

""" Driver Code for Task 2
user = User("Bob", 1234, "password")
print(user.name, user.pin, user.password)
user.change_name("Bobby"), user.change_pin(
    1234), user.change_password("newpassword")
print(user.name, user.pin, user.password) """

# bank user class to perform different transactions


class BankUser(User):
    def __init__(self, name, pin, password):
        self.balance = 0
        super().__init__(name, pin, password)

    #   method to show total balance of the user
    def show_balance(self):
        print(f'{self.name} has an account balance of: {self.balance:.2f}')

    # withdraw method to perform on a user account
    def withdraw(self, withdrawal_amt):
        if withdrawal_amt < 0 or withdrawal_amt is str:
            print('Pleas enter a positive number')
        else:
            self.balance = float(self.balance - withdrawal_amt)

    # deposit method to input money into user's account
    def deposit(self, deposit_amt):
        if deposit_amt < 0 or deposit_amt is str:
            print('Please enter a positive number')
        else:
            self.balance = float(self.balance + deposit_amt)

    # transfer money method to send money into another account
    def transfer_money(self, user, transfer_amt):
        counter = True
        # validation to check transfer amount must be a positive number
        if transfer_amt < 0 or transfer_amt is str:
            print('Please enter a positive number.')
        # validation to check transfer amount must be less than account balance
        elif transfer_amt > self.balance:
            print('Transfer amount must be less than balance.')

        # perform the transaction if the conditions are valid
        else:
            print(f'You are transferring ${transfer_amt} to {user.name}')
            pin = int(input('Authentication required\nEnter your PIN: '))
            if pin == self.pin:
                print('Transfer authorized')
                print(f'Transferring ${transfer_amt} to {self.name}')
                self.withdraw(transfer_amt)
                user.deposit(transfer_amt)
                return counter
            print('Invalid PIN. Transaction canceled.')
        return not counter

    # request money method to take money from different user's account
    def request_money(self, user, request_amt):
        counter = True
        # validation to check request amount must be a positive number
        if request_amt < 0 or request_amt is str:
            print('Please enter a positive number.')
        # validation to check the request amount must be less than acccount's balance
        elif request_amt > user.balance:
            print('Request amount must be less than balance.')
        # perform the request transaction if the conditions are met
        else:
            print(f'You are requesting ${request_amt} from {user.name}')
            pin = int(
                input("User authentication is required...\nEnter Bob's PIN: "))

            if pin == user.pin:
                password = input('Enter your password: ')
                if password == self.password:
                    print('Request authorized')
                    print(f'{user.name} sent ${request_amt}')
                    self.deposit(request_amt)
                    user.withdraw(request_amt)
                    return counter
                print('Invalid password. Transaction canceled.')
            else:
                print('Invalid PIN. Transaction canceled.')
        return not counter


""" Driver Code for Task 3 
bank_user = BankUser('Bob', 1234, 'password')
print(bank_user.name, bank_user.pin, bank_user.password, bank_user.balance) """

""" Driver Code for Task 4 
bank_user2 = BankUser('Bob', 1234, 'password')
bank_user2.show_balance()
bank_user2.deposit(1000)
bank_user2.show_balance()
bank_user2.withdraw(500)
bank_user2.show_balance() """

""" Driver Code for Task 5 """
bank_user3 = BankUser('Bob', 1234, 'password')
bank_user4 = BankUser('Alice', 5678, 'alicepassword')
bank_user4.deposit(5000)
bank_user4.show_balance()
bank_user3.show_balance()
bank_user4.transfer_money(bank_user3, 500)
bank_user4.show_balance()
bank_user3.show_balance()
bank_user4.request_money(bank_user3, 250)
bank_user4.show_balance()
bank_user3.show_balance()
