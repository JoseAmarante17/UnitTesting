'''
Author: Jose Amarante
Purpose: The code is tested by unittesting
Date: 6/2/2021
'''
# import modules
import time

def userName(userLogin = 'test'):
    # Creates file named account to store username
    # Prompts user to insert a username
    userFile = open("username.txt", "a")
    userFile.write(userLogin+"\n")
    userFile.close()
    return userLogin


def userPassword(passwordLogin = 'test'):
    # Creates new file to store user passwords
    # prompts user to insert a password
    passwordFile = open("password.txt", "a")
    passwordFile.write(passwordLogin+"\n")
    passwordFile.close()
    return passwordLogin


def admin():
    # initalizes admin password
    user = "admin"
    password = "password123"
    # ask for admin login
    userInput = eval(input("Enter the admin username: "))
    passwordInput = str(input("Enter the admin password: "))
    time.sleep(2)
    print("Wait...")
    time.sleep(3)
    if userInput == user or passwordInput == password:
        # welcomes the admin into the program
        # gives admin access to view all user login
        print("\nWelcome admin\n")
        time.sleep(1)
        print("1: access user info\n2: exit")

        try:
            adminInput = int(input("\nYour choice: "))
        except:
            print("Enter a valid choice")

        if adminInput == 1:
            # gets info from text files
            passwordFile = open("password.txt", "r")
            passwordContent = passwordFile.readlines()
            passwordFile.close()
            usernameFile = open('username.txt', 'r')
            usernameContent = usernameFile.readlines()
            usernameFile.close()

            # displays user login info and removes '\n'
            char = '\n'
            count = 0
            print("\nUsername \t Password")
            print("--------------------------")
            while count < len(usernameContent):
                print(
                    f"{usernameContent[count].rstrip(char)}\t\t{passwordContent[count].rstrip(char)}")
                count += 1
            print("\nThank you for visiting the spaceship.\n")
        else:
            exit()


def verify():
    # displays user login information and ask them to verify
    username = open("username.txt", "r")
    userLogin = username.readlines()
    username.close()
    password = open("password.txt", "r")
    passwordLogin = password.readlines()
    password.close()

    # ask user to verify
    answer = ''
    char = '\n'
    print(f"\nThe user name inputed was: {userLogin[-1].rstrip(char)}")
    print(f"The password inputed was: {passwordLogin[-1].rstrip(char)}")
    answer = input("Enter y if this is correct: ")
    if answer == 'y' or answer == 'Y':
        time.sleep(1)
        print("Thank you for registering\n")
        exit()
    else:
        time.sleep(1)
        print("Please re-enter your new login credentials\n")
        time.sleep(2)
   
