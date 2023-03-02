name = input()

def normalize(name):

    # put your code here
    new_name = []

    for c in name:
        if (c == "é") or (c == "ë"):
            new_name.append("e")
        elif c == "á":
            new_name.append("a")
        elif c == "å":
            new_name.append("aa")
        elif c == "œ":
            new_name.append("oe")
        elif c == "æ":
            new_name.append("ae")
        else:
            new_name.append(c)

    new_name = "".join(new_name)
    return new_name

print(normalize(name))
