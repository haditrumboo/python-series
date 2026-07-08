words = {
    "roshni" : "light",
    "pani" : "water",
    "aagh" : "fire"
}
print(words, type(words))

word= input("enter the word you want meaning of:  ").strip()
print(words.get(word))
