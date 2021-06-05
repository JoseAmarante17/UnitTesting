'''
Date: 6/5/2021
Purpose: Tests the outputs of the userName and userPassword function
Description: Unit Test testing
'''
# requirements for test
# Import unittest from the standard library
# Create a class called TestSum that inherits from the TestCase class
# Convert the test functions into methods by adding self as the first argument
# Change the assertions to use the self.assertEqual() method on the TestCase class
# Change the command-line entry point to call unittest.main()

# import modules
import unittest
from test_main import userName, userPassword


# tests if the correct user name is outputed to the user
class testLogin(unittest.TestCase):
    def test_Username(self):
        # Creates instances of the userName function
        # Input a default value and compare that with what shows up from txt file
        user = userName()
        file = open("username.txt", 'r')
        fileContent = file.readlines()
        file.close()

         # removes last line from file
        newContent = fileContent[:-1]
        file = open('username.txt', 'w')
        file.writelines(newContent)
        file.close()
        # compares value last entered in text file is equal to value returned by function
        self.assertEqual(fileContent[-1].rstrip('\n'), user)

    # tests if the correct password is outputed to the user
    def test_Password(self):
        # Creates instances of the userPassword function
        password = userPassword()
        file = open('password.txt', 'r')
        fileContent = file.readlines()
        file.close()
        
        # removes last line from file
        newContent = fileContent[:-1]
        file = open('password.txt', 'w')
        file.writelines(newContent)
        file.close()

        # compares value last entered in text file is equal to value returned by function
        self.assertEqual(fileContent[-1].rstrip('\n'),password)
        
