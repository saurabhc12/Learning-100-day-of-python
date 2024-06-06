#to handle to error we can used try handler

a = input("enter the number: ")
print(f"multiplication table of {a} is: ")
for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")

# how to handle error using try method
#used for unexpecated error from user this event deal with this type of error

a = input("enter the number: ")
print(f"Multiplication of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("invalid input")



