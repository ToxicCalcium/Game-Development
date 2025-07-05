login = {"Raghav" : "12345"}

while True:
    print("Password App: \n1) Sign up \n2) Log in \n3) Exit")
    choice = int(input())
    if choice == 1:
        username = str(input("Please enter your new username")).strip()
        password = str(input("Please enter your new password")).strip()
        login[username] = password
        print("login details added successfully")

    elif choice == 2:
        username = str(input("Please enter yout current username")).strip()
        if username in login:
            password = str(input("please enter your current password, {}".format(username)))
            if login[username] == password:
                print("Logged in")
            else:
                print("incorrect password")
        else:
            print("incorrect username")
    
    elif choice == 3:
        break
    