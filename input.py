

# input and string in print function 
'''This uses the := (walrus operator) to assign name inside the print function while still using it later in the same statement.'''
print("hi " ,(name := input("enter your name ?")).capitalize(), " how old are you ?",\
      "ohh you are", (age:=int(input("enter yor age"))),"years old")

# line break using with\n
print("hello!\nhello!\nhello!".upper())

#swapping
a=1
b=2
temp = a
print(f"a value is- {a} b value is- {b}")
a,b = b,a
# a = b ,temp = b
print(f"a value is- {a} b value is- {b}")

#type error two diferent data type canot cocatanate

name = "anura"
age = 44
print(name + str(age))

print("hi",(name :=input("enter your name")),"so how are you",name)



