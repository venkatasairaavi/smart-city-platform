from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, email, role):
        self.id = id
        self.email = email
        self.role = role

    def get_id(self):
        return str(self.id)