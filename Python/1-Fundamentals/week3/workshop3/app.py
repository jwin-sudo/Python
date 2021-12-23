# import library from donations_pkg
from donations_pkg import homepage
from donations_pkg import user

# initialize database
database = {"admin": "password123"}
# define an empty list
donations = []
# define an empty string
authorized_user = ""

# a loop to control user input
while True:
    # print user interface
    homepage.show_homepage()
    print()
    # check if the authorized_user is an empty string
    if authorized_user == "":
        print('You must be logged in to donate.')
    else:
        print('Logged in as: ', authorized_user)

    # ask user to input
    choice = input('Choose an option: ')
    print()

    # ask user to log in
    if choice == "1":
        username = input('Enter username: ')
        password = input('Enter password: ')
        authorized_user = user.login(database, username.lower(), password)

    # register an account
    elif choice == "2":
        username_2 = input('Enter username: ')
        password_2 = input('Enter password: ')
        authorized_user = user.register(database, username_2, password_2)
        if authorized_user is not "":
            database[username_2] = password_2

    # ask user for a donation
    elif choice == "3":
        if authorized_user == "":
            print('You are not logged in.')
            continue

        donation = homepage.donate(authorized_user)
        donations.append(donation)

    # show donation
    elif choice == "4":
        homepage.show_donations(donations)

    # exit the program
    elif choice == "5":
        print('Leaving DonateMe...')
        exit()
    print()
