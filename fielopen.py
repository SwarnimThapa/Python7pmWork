x = open('afile.txt', 'a')
regemail = "Admin123@gmail.com"
regpass = "@Admin321"
email =input("Enter your email.")
password = input("Enter your password.")

if email == regemail and password == regpass:
    print("You have entered the correct email and password.")
    log = f"Email {regemail} and Password {password}"
    x.write(log)
    x.write("\n")
elif email != regemail and password != regpass:
    print("You have entered the wrong email and password.")
    log = f"There was a log in attempt but they inputted the wrong email and password."
    x.write(log)
    x.write("\n")
elif email != regemail and password == regpass:
    print("You have entered the wrong email or password.")
    log = f"There was a log in attempt but they inputted the correct password but the wrong email."
    x.write(log)
    x.write("\n")
elif email == regemail and password != regpass:
    print("You have entered the wrong email or password.")
    log = f"There was a log in attempt but they inputted the correct email but the wrong password."
    x.write(log)
    x.write("\n")