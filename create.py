import pandas as pd
import os


def create_user_forced(username, mail):
    cmd = f'docker-compose exec -e RAILS_ENV=production mastodon_web tootctl accounts ' \
          f'create "{username}" --email "{mail}" ' \
          f'--confirmed --reattach --force >> passwords.txt'
    # os.system(cmd)
    print(f'Done with user: {username}  {mail}')


def write_user_info(username, email):
    text = f'\nUser: {username} \nEmail: {email} \nPassword output: \n'
    with open('passwords.txt', 'a') as f:
        f.write(text)


def create_info_dict(firstname, username, password):
    name = firstname[0:3] + username
    return {
        'user': name,
        'mail': f'{name}@trustfirst.mobi',
        'password': password
    }


# reset passwords.txt info
filename = 'passwords.txt'

with open(filename, 'w') as f:
    f.write('')

# get users from excel
spreadsheet = 'TrustFirstUsers.xlsx'
df = pd.read_excel(spreadsheet)
users_info = [create_info_dict(firstname.lower(), username.lower(), password) for firstname, username, password in zip(df['First Name'], df['Username'], df['Password'])]

print(f"Users to create: {len(users_info)}")

unique_usernames = []

# create users
for info in users_info:

    username = info['user']
    mail = info['mail']
    
    if username not in unique_usernames:
        unique_usernames.append(username)
    else:
        print(f"Duplicate {username}")
        username = username[0] + username
        mail = username[0] + mail
        
    write_user_info(username, mail)    
    create_user_forced(username, mail)

print(f"\nUnique accounts created: {len(unique_usernames)}")

