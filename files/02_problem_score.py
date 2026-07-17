# import random
# you = int(input("enter you score:   "))
# computer = random.randint(1, 50)
# def game(y):
#     with open("file/hscore.txt") as f:
#         content = f.read()
#         if content!= "":
#             content = int(content)
#         else:
#             content = 0

#     print(f"you choose {y} and computer choose {computer}")

#     if y > computer:
#         with open("file/hscore.txt", "w") as f:
#             f.write(str(y))
#     else:
#         print("you loose")
        


# (game(you))



you = int(input("Enter your score: "))

def game(score):
    with open("file/hscore.txt", "r") as f:
        content = f.read()

        if content != "":
            high_score = int(content)
        else:
            high_score = 0

    if score > high_score:
        with open("file/hscore.txt", "w") as f:
            f.write(str(score))
        print("New High Score!")
    else:
        print("High score not broken.")

game(you)
