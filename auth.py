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

def authem(user,psswd,pwdb):
    if user in pwdb and pwdb[user]==psswd:
        print('User Authentified')
    else:
        print('Access Denied')
        sign_up=input('Do you want to Sign up?[Y/N]')
        if sign_up=="Y" or sign_up=="y":
            # user,psswd=get_credentials()
            add_user(user,psswd,pwdb)
            write_pwdb(pwdb)
            print('User: ',user,' created')
        else:
            print('Bye')
    return pwdb

if __name__ == '__main__':
    pwdb = read_pwdb()
    user, password = get_credentials()
    authem(user,password,pwdb)
    #add_user(user, password, pwdb)
    #write_pwdb(pwdb)
