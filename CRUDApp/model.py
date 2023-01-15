class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


users = []
def registerUser(name, email, password):
    user = User(name, email, password)
    users.append(user)
    return "Registered Successfully..."
