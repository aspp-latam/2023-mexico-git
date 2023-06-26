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

def authenticate(user, password, pwdb):
    if user in pwdb:
        if password == pwdb[user]:
            print("Authentification successfull")
        else:
            print("Authentification failed")
    else: 
        add_user(user, password, pwdb)   


if __name__ == '__main__':
    pwdb = read_pwdb()
    user, password = get_credentials()
    authenticate(user, password, pwdb)
    write_pwdb(pwdb)
