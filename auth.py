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
    
def check_user(user, password, pwdb):
    if user in pwdb:
        if pwdb[user] == password:
            print("Successfully authenticated")
        else:
            print("Wrong password.")
    else:
        ans = input('User not found, add the user? (y/n)')     
        if(ans == "Y" or ans == "y"):
            add_user(user, password, pwdb)
            write_pwdb(pwdb)                    
        else:
            print("Not added, have a nice day.")
            
if __name__ == '__main__':
    pwdb = read_pwdb()
    user, password = get_credentials()
    check_user(user, password, pwdb)
# 	q
#    add_user(user, password, pwdb)
#    write_pwdb(pwdb)
