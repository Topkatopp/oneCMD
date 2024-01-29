while True:
    sys = input(">> ")
    if sys.startswith("echo ") == True:
        sys = sys.replace("echo ", "", 1)
        print(sys)
    