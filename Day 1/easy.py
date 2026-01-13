def check_number(num):
    if num>0:
        return print(f"The number {num} is Positive.")
    elif num<0:
        return print(f"The number {num} is Negative.")
    else:
        return print(f"The Number is Zero")    
    
check_number(32)    


num = int(input("Enter a number: "))
print(f"The square of {num} is {num*num}")


num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
print(f"The sum of {num1} and {num2} is {num1+num2}")


name=input("Enter your name: ")
age=input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")


def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False
    
print(is_even(32))


def square(n):
    return n*n

print(square(12))


def add_numbers(a, b):
    return a+b

print(add_numbers(2,5))


num=10
while num!=0:
    print(num)
    num-=1


num = int(input("Enter a number: "))
for i in range (1,11):
    print(f"{num} x {i} = {num*i}")


for i in range(1,11):
    print(i)


num = int(input("Enter a number more than 0: "))
if num%2 == 0:
    print("The number is even")
else:
    print("The Number is odd")    


age = int(input("Enter a age: "))
if age>= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote.")    


num = int(input("Enter a number: "))
if num>0:
    print(f"The number {num} is Positive.")
elif num<0:
    print(f"The number {num} is Negative.")
else:
    print(f"The Number is Zero")    


a=6
b=10
print("Before swapping")
print(f"a is {a}" )
print(f"b is {b}" )
print("After swapping")
a=b+a
b=a-b
a=a-b
print(f"a is {a}" )
print(f"b is {b}" )


a= 1
b= "2"
print(a+int(b))

age = 21
height = 163.5
is_student = True

print(age, height, is_student, type(age),type(height),type(is_student))


name = "Muskan"
print(name)
