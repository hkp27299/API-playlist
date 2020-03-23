from user import User
from werkzeug.security import safe_str_cmp



def auth(username,password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    id = payload['identity']
    return User.find_by_id(id)
