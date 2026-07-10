
while True:
  grades = int(input("Enter your grade: "))

  if 90 <= grades <= 100:
    print("Excellent")
  elif 80 <= grades < 90:
    print("You have got grade 'A'")
  elif 70 <= grades < 80:
    print("You have got grade 'B'")
  elif 50 <= grades < 70:
    print("You have got grade 'C'")
  else:
     print("You need to work hard.") 
  choise = input("do you want to enter another grade? (yes/no): ") 
  if choise.lower() == "no":
    break  