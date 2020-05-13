from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Users:
    """Users model"""

    def __init__(self,email, password):
        """ Initializing user attributes """
        self.email = email
        self.password = password
    
    def get_user_by_email(email):
        """Getting the user against their email address"""
        get_user_by_email= """
        SELECT userId,email,password from users 
        where users.email ='{}'""".format(email)
        return db.handle_select_queries(get_user_by_email)
    
    def compare_password(hashed_password,password):
        """Helps compare a plain string password against its hash
        returns true or false"""
        return check_password_hash(hashed_password,str(password))
    
    
    
     