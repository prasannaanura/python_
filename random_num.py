

playing = input("do you like to play if yes type(Y/N)").upper()
score = 0
if playing == "Y":
    print("Lets paly!")
#elif playing == "N":
    #quit("see you again!")
    question = input("what is stanrd for cpu ?")
    if question.lower() == "central processing unit":
        print("corect!")
        score += 1
        print(f"your score is :{score}")
    else:
        print("incorect!")
  
    question2 = input("what is stanrd for RAM ?")
    if question2.lower() == "random access memory":
        print("corect!")
        score += 2
        print(f"your score is :{score}")
    else:
        print("incorect!")
       

else:
    quit("see you!")
    


 # type: ignore