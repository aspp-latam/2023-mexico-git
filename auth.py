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

def check_psw(user, password, pwdb):
    if pwdb[user] == password:
        print('Successfully authenticated!')
    else:
         print('Wrong password!')


def add_user(user, password, pwdb):
    if user not in pwdb:
        pwdb[user] = password
    return pwdb


if __name__ == '__main__':
    pwdb = read_pwdb()
    user, password = get_credentials()
    add_user(user, password, pwdb)
    write_pwdb(pwdb)
    check_psw(user, password, pwdb)
