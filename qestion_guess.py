questions = ("how many elements in periodic table ? ",
            "what ia the largest river in the world ? ",
            "who is the popular German Idealist ? ",
            "What is the large oacean in the world ? ")

options = (("A.116","B.123","C.167","D.115"),
         ("A. Amozon","B.NYLE","C.GANAGA","D.MAHAVWALI"),
         ("A.Kant","B.Marks","C.Hegel","D.Lacan"),
         ("A.Indian","B. Pasific","C. kaspian","D.Red sea"))

answers = ("A","B","C","A")

guesess = []
score = 0
question_num = 0

for qestion in questions:
    print("-----------------------------")
    print(qestion)
    for option in options[question_num]:
     print(option)
     
    guess = input("Enter your answer 'A,B,C,D':").upper()
    guesess.append(guess)
    if guess == answers[question_num]:
        print("answer is correct")
        score += 1
    else:
       print("answer is incorect")
    question_num += 1

print("...............................")
print("              Result           ")
print("...............................")

print("Answers: ",end="")
for answer in answers:
   print(answer,end=",")
   
print()
print("guesses: ",end="")
for guess in guesess:
   print(guess,end=",")
   
print()
   

print(f"your score is: {score}")
score = int(score/len(questions)*100)
print(f"your score is : {score}%")

