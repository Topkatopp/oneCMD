def crypto(file):
    try:
        with open(file, "r", encoding="UTF-8") as f:
            text = f.read()
    except:
        text = file
    for i in range(3):
        text = text.replace("q", "⁜");text = text.replace("w", "™");text = text.replace("e", "⁂");text = text.replace("r", "π");text = text.replace("t", "Π");text = text.replace("y", "⁸");text = text.replace("u", "₥");text = text.replace("i", "௹");text = text.replace("o", "↶");text = text.replace("p", "®");text = text.replace("å", "⁂");text = text.replace("¨", "⁅");text = text.replace("^", "⁆");text = text.replace("~", "↉");text = text.replace("a", "⇞");text = text.replace("s", "©");text = text.replace("d", "₺");text = text.replace("f", "⟬");text = text.replace("g", "⟫");text = text.replace("h", "‖");text = text.replace("j", "✓");text = text.replace("k", "₧");text = text.replace("l", "৻");text = text.replace("ö", "₻");text = text.replace("ä", "ℳ");text = text.replace("'", "₷");text = text.replace("*", "₰");text = text.replace("<", "↪");text = text.replace(">", "↩");text = text.replace("z", "₿");text = text.replace("x", "Ⅶ");text = text.replace("c", "⇔");text = text.replace("v", "ʡ");text = text.replace("b", "⇶");text = text.replace("n", "▮");text = text.replace("m", "⨗");text = text.replace(",", "▭");text = text.replace(";", "⨌");text = text.replace(".", "◄");text = text.replace(":", "⁐");text = text.replace("-", "∀");text = text.replace("_", "◊");text = text.replace("+", "⁼");text = text.replace("?", "ⅷ");text = text.replace("\\", "ⅲ");text = text.replace("/", "≍");text = text.replace("(", "ↈ");text = text.replace(")", "⨭");text = text.replace('"', "◫")
    return text

def decrypt(file):
    try:
        with open(file, "r", encoding="UTF-8") as f:
            text = f.read()
    except:
        text = file
    text = text.replace("⁜", "q")
    text = text.replace("™", "w")
    text = text.replace("⁂", "e")
    text = text.replace("π", "r")
    text = text.replace("Π", "t")
    text = text.replace("⁸", "y")
    text = text.replace("₥", "u")
    text = text.replace("௹", "i")
    text = text.replace("↶", "o")
    text = text.replace("®", "p")
    text = text.replace("⁂", "å")
    text = text.replace("⁅", "¨")
    text = text.replace("⁆", "^")
    text = text.replace("↉", "~")
    text = text.replace("⇞", "a")
    text = text.replace("©", "s")
    text = text.replace("₺", "d")
    text = text.replace("⟬", "f")
    text = text.replace("⟫", "g")
    text = text.replace("‖", "h")
    text = text.replace("✓", "j")
    text = text.replace("₧", "k")
    text = text.replace("৻", "l")
    text = text.replace("₻", "ö")
    text = text.replace("ℳ", "ä")
    text = text.replace("₷", "'")
    text = text.replace("₰", "*")
    text = text.replace("↪", "<")
    text = text.replace("↩", ">")
    text = text.replace("₿", "z")
    text = text.replace("Ⅶ", "x")
    text = text.replace("⇔", "c")
    text = text.replace("ʡ", "v")
    text = text.replace("⇶", "b")
    text = text.replace("▮", "n")
    text = text.replace("⨗", "m")
    text = text.replace("▭", ",")
    text = text.replace("⨌", ";")
    text = text.replace("◄", ".")
    text = text.replace("⁐", ":")
    text = text.replace("∀", "-")
    text = text.replace("◊", "_")
    text = text.replace("⁼", "+")
    text = text.replace("ⅷ", "?")
    text = text.replace("ⅲ", "\\")
    text = text.replace("≍", "/")
    text = text.replace("ↈ", "(")
    text = text.replace("⨭", ")")
    text = text.replace('◫', '"')

    return text

if __name__ == "__main__":
    print("".replace(";", "\n"))
    text = 'test.py'
    test = crypto(text)
    print(test)
    test = decrypt(test)
    print(test)

    if text == test:
        print("ok")
    else:
        print("error")
