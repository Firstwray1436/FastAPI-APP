#a function is a reusable block of code 
# istead of writing same logic againa and again :
#you define once->reuse anytime

def greet():
    print("hello")

greet()  # caliing


#function with parameters

def greet(name):
    print("hello",name)

greet("pratham")


#return vs print

def add(a,b):
    print(a+b)

add(5,3)


#using return


def add(a,b):
    return a+b

result = add(2,3)

print(result)

new_result=add(4,6)

print(new_result)

#🧠 Rule

#👉 print = show
#👉 return = give back value


def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "cannot divide by zero"
    
print(divide(5,6))

print(divide(18,4))

print(divide(17,0))

