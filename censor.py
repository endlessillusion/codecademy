def censor(text, cens):
    result = ""
    string = str.split(str(text))
    count = 1
    space = " "
    for word in string:
        if count == len(string):
            space = ""
        if word.lower() == cens.lower():
            result = result + "*" * len(word) + space
        else:
            result = result + word + space
        count = count + 1
    return result
