# model/user.py

class User:
    def __init__(self, user_id: str, name: str, email: str, password: str):
        self.user_id = user_id      # ID único en Firebase
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        """Convierte el usuario a diccionario para Firebase"""
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
