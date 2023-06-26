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
    
    
def authenticate(pwdb): 
    user, password = get_credentials()
    if user in pwdb:
        if pwdb[user] == password:
           print("Successfully authenticated!")
        else:
           print("Wrong password!")
    else:
        print("The user does not exist, please:")
        user, password = get_credentials()
        add_user(user, password, pwdb)
    
    return pwdb


if __name__ == '__main__':
    pwdb = read_pwdb()

    pwdb = authenticate(pwdb)
    
    write_pwdb(pwdb)
