'''
-1 rock
0 paper
1 scissor

'''
import random

choose = input("choose (r/p/s):  ").strip().lower()

dic = {
    "r": -1,
    "p": 0,
    "s": 1
}
reversedic = {
    -1: "rock",
     0: "paper",
     1: "scissor"
}
computer = random.choice([-1, 0, 1])

if choose not in dic:
    print('invalid input.')
    exit()


choose = dic[choose]

print(f"you choose {reversedic[choose]}/n compter choose {reversedic[computer]}" )


if computer == choose:
    print("its draw")
else:
    if computer == -1 and choose == 0:
        print("you win!")
    elif computer == -1 and choose ==1:
        print("comuter win!")
    elif computer == 0 and choose == -1:
        print("comuter win!")
    elif computer == 0 and choose == 1:
        print("you win!")
    elif computer == 1 and choose == -1:
        print("you win!")
    elif computer == 1 and choose == 0:
        print("computer win!")
    
    else:
        print("something went wrong.")

