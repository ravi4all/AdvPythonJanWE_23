import controller

def registerUser():
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    pwd = input("Enter your password : ")
    msg = controller.registerController(name, email, pwd)
    print(msg)

def loginUser():
    pass

def main():
    print("""
    1. Login
    2. Register
    """)

    ch = input("Enter your choice : ")
    operations = {
        "1" : loginUser,
        "2" : registerUser
    }
    operations.get(ch)()

main()