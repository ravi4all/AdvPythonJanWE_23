import model

def registerController(name, email, pwd):
    msg = model.registerUser(name, email, pwd)
    return msg

def validateEmailController(email):
    msg = model.validateEmail(email)
    return msg