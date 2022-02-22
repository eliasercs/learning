_users = []

def get_user(username):
    for user in _users:
        if user.username == username:
            return user
    return None