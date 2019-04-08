import unittest
import pyperclip
import random
import string
from users import User
from users import credentials

class Testuser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
        # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Tash","Gmail") # create contact object


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Tash")
        self.assertEqual(self.new_user.account_name,"Gmail")
        

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

# setup and class creation up here
    
# Items up here...

   

# More tests above
    # def test_delete_user(self):
    #         '''
    #         test_delete_user to test if we can remove a user from our user list
    #         '''
    #         self.new_user.save_user()
    #         test_user = user("Tash","Gmail") # new user
    #         test_user.save_user()

    #         self.new_user.delete_user()# Deleting a User object
    #         self.assertEqual(len(user.user_list),1)

   
        
    # def test_display_all_users(self):
    #     '''
    #      method that returns a list of all users saved
    #      '''

    #     self.assertEqual(user.dispaly_user(),user.user_list)

        

if __name__ == '__main__':
    unittest.main()