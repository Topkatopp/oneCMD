def init_user():
    with open("data\\user.dat", "r") as f:
        return f.read()
