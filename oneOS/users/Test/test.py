with open("users\\Test\\hi.py", "w") as f:
    f.write("""while True:
    sys = input(">> ")
    if sys.startswith("echo ") == True:
        sys = sys.replace("echo ", "", 1)
        print(sys)
    """)
with open("users\\Test\\hi.py", "r") as f:
    aaaa = f.read()
print(aaaa)
exec(aaaa)
