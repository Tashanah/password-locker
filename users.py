class user:
    '''
    class that generates new instance of a user
    '''
    # user_list=[]

    def _init_(self,user_name,account_name):
        self.user_name=user_name
        self.account_name=account_name
print("enter username")
name=input()
print("account name")
account=input()

class credentials:
    '''
    class that generates new password
    '''
    # credentials_list=[]
    def _init_(self,user_password):
        self.user_password=user_password 
print("enter password.It must be a mix of 12 numbers and letters(uppercase and lowercase)")
password=input()
