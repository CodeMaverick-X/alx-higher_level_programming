#!/usr/bin/python3
def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new = ""

    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            new = new + text[i]
            new = new + "\n"
            new = new + "\n"

        elif text[i] != " ":
            new = new + text[i]
        else:
            if text[i -1] in ".:? ":
                new = new + ""
            else:
                new = new + text[i]

    print(new, end="")
