from flask import current_app
from models.user import User
from datalayers.user_datalayer import get_user, store_user

def add_user(user: User):
    """
    checks all parameters and adds user to the storage
    """
    # the user can be stored with the corresponding foreign keys.
    result = store_user(user)
    return result

def find_user_by_id(user_id: int):
    """
    Searches for a userId in the database to check if a user exists.
    """

    result = get_user(user_id)
    if(len(result) == 1):
        return True

    return False