word = "donkey"

def find_word(word):
    with open("files/donkey.txt") as f:
        a = f.read()

    if word in a:
        print(word)
        a = a.replace(word, "horse")
        print(a)
    else:
        print("word not found.")

find_word(word)