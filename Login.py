email = input("Hello, please enter your email to log into the site.")
password = input("Now, enter your password to log in.")

siteEmail = "admin@gmail.com"
sitePassword = "Admin@123"

if email == siteEmail and password == sitePassword:
    print("You entered the correct email and password.")
elif email != siteEmail:
    print("You enterted the wrong email.")
elif password != sitePassword:
    print("You entered the wrong password.")
elif email != siteEmail and password != sitePassword:
    print("You entered the wrong email and password.")


