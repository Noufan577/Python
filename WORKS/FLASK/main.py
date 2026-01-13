class User:
    def __init__(self, name):
        self.name = name
        self.is_loggedin = False

    # decorator
    def authenticator(function):
        def wrap(self, *args, **kwargs):
            if self.is_loggedin:
                return function(self, *args, **kwargs)
            else:
                print("User not logged in. Cannot create post.")
        return wrap

    @authenticator
    def create_post(self):
        print(f"Post created by user {self.name}")


# create user
u1 = User("Noufal")

# try without login
u1.create_post()

# login user
u1.is_loggedin = True

# try again
u1.create_post()
