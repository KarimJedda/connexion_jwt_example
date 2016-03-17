from werkzeug.security import safe_str_cmp

class User(object):
    def __init__(self, id, username, password, admin):
        self.id = id
        self.username = username
        self.password = password
        self.admin = admin

    @property
    def is_admin(self):
            return self.admin

    def __str__(self):
        return "User(id='{}', admin='{}')".format(self.id, self.admin)

users = [
    User(1, 'user1', 'abcxyz', True),
    User(2, 'user2', 'abcxyz', False),
    User(23, 'user3', 'abcxyz', False),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    user = userid_table.get(user_id, None)
    return user