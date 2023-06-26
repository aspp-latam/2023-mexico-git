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

def authenticate_user(user, password, pwdb):
    authenticate  = False
    while authenticate == False:
        if pwdb[user] == password:
            authenticate = True    
            print("Welcome ", user)
        else:
            print("Your password is not correct, try again")  
            password = input('Type password: ')


if __name__ == '__main__':
    pwdb = read_pwdb()
    user, password = get_credentials()
    add_user(user, password, pwdb)
    authenticate_user(user, password, pwdb)
    write_pwdb(pwdb)
