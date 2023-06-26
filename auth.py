import json

def get_credentials():
    user = input('Type user name: ')
    password = input('Type password: ')
    return user, password

def write_pwdb(pwdb):
    fn = 'database.json'
    with open(fn, 'w') as f:
        json.dump(pwdb, f)

def read_pwdb():
    try:
        with open('database.json', 'r') as f:
            pwdb = json.load(f)
    except FileNotFoundError:
        pwdb = {}
    return pwdb

def add_user(user, password, pwdb):
    if user not in pwdb:
        pwdb[user] = password
    return pwdb

def authenticate_user(pwdb):
    user = input('Type user name: ')
    
    if user in pwdb:
        print("user is in database")
        input_password = input('Type password: ')
        stored_password = pwdb[user]
        # we compare the stored password with the one provided by the user
        if input_password == stored_password:
            print("Password is correct!")
        else:
            print("Incorrect password!")
    else:
        print("user not in database")

if __name__ == '__main__':
    pwdb = read_pwdb()
    # print(pwdb)
    # user, password = get_credentials()
    # add_user(user, password, pwdb)
    # write_pwdb(pwdb)
    authenticate_user(pwdb)

    
