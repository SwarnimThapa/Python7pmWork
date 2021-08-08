#To create the txt file.
import os.path
#To hide password.
import getpass

if not os.path.exists('db.txt'):
    fs = open('db.txt', 'w')
    fs.close()
def register():
    print("============= Register =============")
    emailreg = input("Enter email: ")
    if emailreg in open('db.txt').readlines():
        print("Email is already taken.")
    passreg = getpass.getpass("Enter password: ")
    passconfirm = getpass.getpass("Confirm your password: ")
    if passreg == passconfirm:
        print("The password is correct.")
    elif passreg != passconfirm:
        print("Invalid password.")
    handle = open('db.txt', 'a')
    handle.write(emailreg)
    handle.write(" ")
    handle.write(passreg)
    handle.write("\n")
    handle.close()
    print("You have sucessfully register a account.")
    return
def login():
    print("============= Login =============")
    email = input("Enter email: ")
    password = input("Enter password: ")
    get_record = open('db.txt','r').readlines()
    userdata = []
    for user in get_record:
        userdata.append(user.split())
    totaluser = len(userdata)
    increment = 0
    loginsucess = False
    while increment<totaluser:
        uemail = userdata[increment][0]
        upassword = userdata[increment][1]
        if uemail == email and password == upassword:
            loginsucess = True
        increment+=1
    if loginsucess == True:
        print("Welcome.")
    elif loginsucess == False:
        print("Your email or password are incorrect.")
question = input("Do you have a account? y/n: ")
if question == 'y':
    login()
elif question == 'n':
    register()
else:
    print("Enter a valid option please.")

