names = ["kevin","joe","peter","matt","marck"]
ages = [23,11,43,26,28]
name = input("Enter a name: ")
age = int(input("Enter age: "))
names.append(name)
ages.append(age)

for name,age in zip(names,ages):
    if age > 55:
        break
    if age < 12:
        continue
    
    print(f"{name.title():<6} is {age:>3} years old,")
