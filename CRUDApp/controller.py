import model

def registerController(name, email, pwd):
    msg = model.registerUser(name, email, pwd)
    return msg