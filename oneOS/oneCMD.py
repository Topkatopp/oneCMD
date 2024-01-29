import modules.runing
import modules.crypto
import modules.antivirus
import os


with open("outlog\\outlog.out", "w") as f:
    f.write("")

def change_outlog(text):
    with open("outlog\\outlog.out", "r") as f:
        outlog = f.read()
    with open("outlog\\outlog.out", "w") as f:
        f.write(outlog + "\n" + text)

def outlog():
    with open("outlog\\outlog.out", "r") as f:
        return f.read()

def text_help():
    with open("command/commands.help", "r") as f:
        return f.read()


while True:
    print("\u001b[31m" + "[runing.init_user(): init users!]")
    change_outlog("[runing.init_user(): init users!]")
    users = modules.runing.init_user()
    users = users.split("\n")
    userss = users[0].split(";")
    prev = userss[1]
    user = userss[0]
    path = fr"users\{user}"
    try:
        with open(path + r"\work.dat", encoding="UTF-8") as f:
            a = f.read()
            f.close()
        print(a)
    except FileNotFoundError as f:
        print(f"[kernel: NOT founded user {user} path so creating it]")
        change_outlog(f"[kernel: NOT founded user {user} path so creating it]")
        os.mkdir("users\\" + user)
        with open(f"users\\{user}\\work.dat", "w") as ff:
            ff.write("")
        passw = input(f"[kernel: write a password for user {user} write nothing to set global account]>> ")
        change_outlog(f"[kernel: write a password for user {user} write nothing to set global account]>> ")



        if passw == "":
            pass
        else:
            passw = modules.crypto.crypto(passw)
            with open(f"users\\{user}\\pass.dat", "w", encoding="UTF-8") as fff:
                fff.write(passw)
        continue

    try:
        with open(path + r"\pass.dat", "r", encoding="UTF-8") as f:
            password = f.read()
        password = modules.crypto.decrypt(password)
        while True:
            ispassword = input("write password to account or write nothing to run from guest>> ")
            change_outlog("write password to account or write nothing to run from guest>> ")
            if ispassword == "":
                prev = "3"
                user = "GUEST"
                break
            elif ispassword == password:
                print("correct password!")
                change_outlog("correct password!")
                break
            else:
                print("incorrect password! try again.")
                change_outlog("incorrect password! try again.")

    except FileNotFoundError as f:
        print(f"[kernel: user {user} password not founded so running without password]")
        change_outlog(f"[kernel: user {user} password not founded so running without password]")
        pass

    break

variables = {
    "%user%":f"{user}",
    "%prev%":f"{prev}"
}

print("""
""" * 100 + "\u001b[37m")
while True:
    sys = input()
    if sys == "cls":
        print("""
""" * 100)
    elif sys.startswith("echo ") == True:
        sys = sys.replace("echo ", "", 1)
        if sys in variables:
            echo_sys = variables[sys]
            sys = sys.replace(sys, echo_sys)

        print(sys)
    elif sys.startswith("set ") == True:
        sys = sys.replace("set ", "", 1)
        sys = sys.split(" = ")
        if sys[0].startswith("%") == False and sys[0].endswith("%") == False:
            print("\u001b[31m" + f"ERROR wrong format of variable: {sys[0]} [use the %name_variable%]" + "\u001b[37m")
        variables[sys[0]] = sys[1]
    elif sys.startswith("outlog") == True:
        sys = sys.replace("outlog", "", 1)
        if sys == "":
            print(outlog())
        elif sys.startswith(" add") == True:
            sys = sys.replace(" add ", "", 1)
            change_outlog(sys)
    elif sys == "dir":
        print(os.listdir(path))
    elif sys.startswith("mkdir ") == True:
        if "open(" in sys or ")" in sys or "as" in sys or "," in sys or "\"" in sys:
            print("ERROR: the file name is incorrect")
            continue
        sys = sys.replace("mkdir ", "", 1)
        path_mkdir = sys
        os.mkdir(path + "\\" + path_mkdir)
    elif sys.startswith("mkfile ") == True:
        sys = sys.replace("mkfile ", "", 1)
        if not " & " in sys:
            if "open(" in sys or ")" in sys or "as" in sys or "," in sys or "\"" in sys:
                print("ERROR: the file name is incorrect")
                continue
            path_file = sys
            with open(path + "\\" + path_file, "w") as f:
                f.write("")
        else:
            sys = sys.split(" & ")
            if "open(" in sys[0] or ")" in sys[0] or "as" in sys[0] or "," in sys[0] or "\"" in sys[0]:
                print("ERROR: the file name is incorrect")
                continue
            path_file = sys[0]
            text = sys[1]
            text = text.replace("\\n", "\n")
            with open(path + "\\" + path_file, "w") as f:
                f.write(text)
    elif sys == "help":
        print(text_help())

    elif sys.startswith("python ") == True:
        sys = sys.replace("python ", "", 1)
        if "open(" in sys or ")" in sys or "as" in sys or "," in sys or "\"" in sys:
            print("ERROR: the file name is incorrect")
            continue
        with open(path + "\\" + sys) as f:
            text = f.read()
        result = modules.antivirus.anti_virus_file(text)
        if result == "":
            pass
        else:
            print(f"the file need to access [{result}] give access? [Y/N]")
            syss = input("[Y/N]>> ")
            if syss == "Y":
                pass
            else:
                continue
        try:
            exec(text)
        except Exception as exc:
            print(exc)




