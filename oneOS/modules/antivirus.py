def anti_virus_file(text):
    text = text.split("\n")
    result = ""
    for i in text:
        if "open(\"" in i:
            i = i.replace("open(", "", 1)
            i = i.replace("with ", "", 1)
            i = i.split("as")
            i = i[0]
            print(i)
            i = i.replace(")", "", 1)
            i = i.replace("\"", "")
            i = i.split(",")
            result += i[0] + "\n"
    if result == "":
        return ""
    return "oneOS\\" + result
