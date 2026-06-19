def main():
    text = input("camelCase: ")
    check_upper(text)


def check_upper(text):
    box = ""
    for letter in text:
        if letter.isupper():
            box = box + "_" + letter.lower()
        else:
            box = box + letter
    print(box.strip("_"))           

main()
