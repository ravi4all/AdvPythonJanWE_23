import controller

def registerUser():
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    msg = controller.validateEmailController(email)
    if msg == "no":
        pass
    else:
        print("Email Already Exists")
        main()
    pwd = input("Enter your password : ")
    msg = controller.registerController(name, email, pwd)
    print(msg)

def loginUser():
    email = input("Enter your email : ")
    pwd = input("Enter your password : ")


def main():
    while True:
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