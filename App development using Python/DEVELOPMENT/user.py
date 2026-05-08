class User:
    def __init__(self,enrollment_id : str,password:str):
        
        self.enrollment_id = enrollment_id
        
        self.password= password

    

    def get_userpassw(self):
        return self.password
    
    def get_enrollment_id(self):
        return self.enrollment_id
    
    
    


class NewUser(User):
    def __init__(self,name:str,enrollment_id : str,account_type:str,email:str,password:str,confirmed_password:str):
        super().__init__(enrollment_id,password)
        self.name= name
        self.account_type=account_type
        self.email = email
        self.confirmed_password = confirmed_password

    def get_user_name(self):
        return self.name

    def get_user_email(self):
        return self.email

    def get_confirmed_passw(self):
        return self.confirmed_password
    
    def get_user_account_type(self):
        return self.account_type
    
    def get_user_data(self):
        return{
            'enrollment_id': self.enrollment_id,
            'name': self.name,
            'account_type':self.account_type,
            'email': self.email,
            'password': self.password,
            'confirmed_password': self.confirmed_password}