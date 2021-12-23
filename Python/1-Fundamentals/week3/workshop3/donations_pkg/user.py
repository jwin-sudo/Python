# function to login and double checking key and value in the dictionary
def login(database, username, password):
    # check if the username is a key in the database and the password is in the database
    if username in database.keys() and password in database.values():
        print('Welcome back admin!')
        return username

    # check if the username is in the database and the password is not in the database
    elif username in database and database[username] is not password:
        print('Incorrect password for admin.')
        return ""
    # check if the username is not in the database
    elif username not in database:
        print('User not found. Please register.')
        return ""

# function to register an account with some restrictions


def register(database, username, password):
    # convert username to lowercase and check the length of username and password
    if username.lower() in database and len(username) <= 10 and len(password) <= 5:
        print('Username already registered.')
        return ""
    # invalid if username is greater than 10 and password greater than 5
    elif len(username) > 10 and len(password) > 5:
        print('Username cannot be over 10 characters, and password must be at least 5 characters.')
    # print out username
    else:
        print(f'Username {username} registered!')
        return username
