# #!/usr/bin/env python3.6
# import unittest
# import random
# import string
# from users import user
# from users import credentials

# def create_user(user_name,account_name):
#     '''
#     Function to create a new user
#     '''
#     new_user = user(user_name,account_name)
#     return new_user

# def create_credential(user_password):
#     '''
#     Function to create a new password
#     '''
#     new_credential = credentials(user_password)
#     return new_credential

# def save_user(user):
#     '''
#     Function to save user
#     '''
#     user.save_user()

# def save_credential(credentials):
#     '''
#     Function to save password
#     '''
#     credentials.save_credential()

# def del_user(user):
#     '''
#     Function to delete user
#     '''
#     user.delete_user()

# def del_credential(credentials):
#     '''
#     Function to delete credential
#     '''
#     credentials.delete_credential()

# def display_user(user):
#     '''
#     Function to display a user
#     '''
#     return user.display_user()

# def display_credential(credentials):
#     '''
#     Function to display a credential
#     '''
#     return credentials.display_credential()

# def main():
#     def _init_(self,user_name,account_name):
#         self.user_name=user_name
#         self.account_name=account_name

# user_name=input("enter username ")

# account_name=input("account name: ")  
# def _init_(self,user_password):
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


# if __name__ == '__main__':
#      unittest.main()   









# # def randomStringDigits(stringLength=6):
# #     password=string.ascii_letters + string.digits
# #     lettersAndDigits = string.ascii_letters + string.digits
# #     return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
# # print (randomStringDigits(12))


