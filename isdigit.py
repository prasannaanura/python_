
while True:
 user_input = input("Enter your age ")
 if user_input.isdigit():

  while True:
    name= input("enter your name ").capitalize()
    if name.replace(" ", "").isalpha():
     print(f" Hi {name} your age is {user_input}.")
     break
    else:
         print("invalid input! please enter only letters")
 break
else:
     print("invalid input !")