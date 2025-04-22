class ChatBook():
    def __init__(self):
        self.usrname = ''
        self.password = ''
        self.loggedin = False

        self.menu()

    def menu(self):
        usr_inp = input(""" Enter your option to proceed:
                            1. Signup
                            2. Signin
                            3. Write a post
                            4. Send message to a friend
                            5. Exit (press any key)
                            --> """)
        if usr_inp == "1":
            self.signup()
        elif usr_inp == "2":
            self.signin()
        elif usr_inp == "3":
            self.write_post()
        elif usr_inp == "4":
            self.send_message()
        else:
            exit()

    def signup(self):
        email = input("Enter your email address: ")
        pswd = input("Setup your password: ")
        self.usrname = email
        self.password = pswd
        print("\n")
        print("You have successfully signed up!")
        print("\n")
        self.menu()

    def signin(self):
        if (self.usrname=="") or (self.password==""):
            print("You need to sign up first!")

        else:
            usr_name = input("Enter you email id: ")
            pswd = input("Enter your password: ")
            if (self.usrname == usr_name) and (self.password == pswd):
                print("You have been logged in successfully!!")
                self.loggedin = True
        print("\n")
        self.menu()

    def write_post(self):
        if self.loggedin == True:
            txt = input("Please type your post here: ")
            print(f"Your Post says: {txt}")
        else:
            print("Please sign in first!")
        print("\n")
        self.menu()

    def send_message(self):
        if self.loggedin == True:
            frnd = input("Whom to send: ")
            txt = input("Type your message here: ")
            print(f"You are sending a message to {frnd}!")
        else:
            print("Please sign in first!")
        print("\n")
        self.menu()

usr = ChatBook()