# def main():
import pyperclip
import random
import string
class User:
    '''
    class that generates new instance of a user
    '''
    user_list=[]

    def __init__(self,user_name,account_name):
        self.user_name = user_name
        self.account_name = account_name



    def delete_user(self):
        '''
        delete user method deletes a username and account name
        '''
        User.user_list.remove(self)
   
    def save_user(self):
        '''
        save user method saves a username and account name
        '''
        User.user_list.append(self)


    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

class credentials:
    '''
    class that generates new password
    '''
    credentials_list=[]

    def __init__(self,user_password):
        self.user_password=user_password 

    def create_credential(self):
        '''
        create credential method creates a new password
        '''
        credentials.credentials_list.append(self)

    def del_credential(self):
        '''
        delete credential method deletes a password
        '''
        credentials.credentials_list.remove(self)
    
    def save_credential(self):
        '''
        save credential method saves a password
        '''
        credentials.credentials_list.append(self)

    def dispaly_credential(self):
        '''
        dispaly credential method allows a user to view all accounts and usernames
        '''
        credentials.credentials_list.append(self)


#         self.user_password=user_password 
# print("type own-to generate your own password or random-to randomly generate a password")
# passwordtype=input()

# if passwordtype=='own':
#     print("enter password")
#     passwordtype=input() 
#     print("your user name is " + user_name, "for " + account_name,"your password is " + passwordtype)
    
# elif passwordtype=='random':
    

#     def randomStringDigits(stringLength):
#         password=string.ascii_letters + string.digits
#         lettersAndDigits = string.ascii_letters + string.digits
#         return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
#         # randomStringDigits(12)

# print("your user name is " + user_name, "for " + account_name," your random password is " + randomStringDigits(12))

