'''
User register, login, logout, display username operations using json
'''
from getpass import getpass
import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.is_logged_in = False
        self.current_user = {}
        self.load_users()

    def load_users(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    new_user = User(username = user['username'], password= user['password'], email = user['email'])
                    self.users.append(new_user)
            print(self.users)
        else:
            return "users.json"

    def register(self, user: User):
        self.users.append(user)
        self.save_to_file()
        print("User registered")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.is_logged_in = True
                self.current_user = user
                print('Log in succesful')
                break
            elif user.username == username and user.password != password:
                print('Wrong password')
                break
            else:
                print('Wrong username')
                break

    def logout(self):
        self.is_logged_in = False
        self.current_user = {}
        print('Logout succesfull')

    def display(self):
        if self.is_logged_in:
            print(f'Logged in with {self.current_user.username}')
        else:
            print('Not logged in!')

    def save_to_file(self):
        user_list = []
        for user in self.users:
            user_list.append(json.dumps(user.__dict__))

        with open('users.json', 'w') as file:
            json.dump(user_list, file)

repository = UserRepository()

while True:
    print("1- Register\n2- Login\n3- Logout\n4- Display Username\n5- Exit")
    choice = input("Please make choice : ")
    if choice == "5":
        break
    else:
        if choice == "1":
            username = input("Username: ")
            password = getpass("Password: ")
            email = input("Email : ")
            user = User(username=username, password=password, email=email)
            repository.register(user)
            #register
        elif choice == "2":
            if repository.is_logged_in:
                print('Already logged in.')
            else:
                username = input('Username : ')
                password = getpass('Password : ')
                repository.login(username, password)

        elif choice == "3":
            repository.logout()
            #logout
        elif choice == "4":
            repository.display()
            #display username
        else:
            print("Wrong choice ! 1-4 ")
