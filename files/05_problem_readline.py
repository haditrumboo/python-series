word = input("Enter word: ").lower()

def read(word):
    with open("files/s.txt", "r") as f:
        found = False

        for line_number, line in enumerate(f, start=1):
            if word in line.lower():
                print(f"'{word}' is present in line {line_number}")
                found = True

        if not found:
            print("Word not present in any line.")

read(word)

# ======================================

word = input("Enter word: ").lower()

with open("files/s.txt", "r") as f:
    line_number = 1
    found = False

    line = f.readline()

    while line != "":
        if word in line.lower():
            print(f"'{word}' is present on line {line_number}")
            found = True

        line = f.readline()
        line_number += 1

    if not found:
        print("Word not present in any line.")
