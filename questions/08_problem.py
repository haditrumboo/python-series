try:
    with open("questions/f/sample.txt", "r") as f:
        line = 0
        char = 0
        sen = ""
        digits = 0
        spaces = 0

        for i in f:
            line += 1
            sen += i

    words = sen.split()

    for i in sen:
        char += 1

        if i.isdigit():
            digits += 1

        if i == " ":
            spaces += 1

    print(f"Lines: {line}")
    print(f"Words: {len(words)}")
    print(f"Characters: {char}")
    print(f"Digits: {digits}")
    print(f"Spaces: {spaces}")

except FileNotFoundError:
    print("File does not exist.")