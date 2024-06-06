
def greet(fx):
    print("Good Morning")
    fx()
    print("Thank you for using this function")
    return fx
@greet
def hello():
    print("hello world")
@greet
def busniss():
    print("this is our startup")

#decoration function help to decorat the object its add the message when we run the object