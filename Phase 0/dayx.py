try:
    a=int(input("enter value of a"))
    b=int(input("enter value of b"))
    operator=input("enter the operator sign(like-+,-,*,/)")

    if operator=="-":
        print(a-b)
    elif operator=="+":
        print(a+b)
    elif operator=="*":
        print(a*b)
    elif operator=="/":
        print(a/b)  
    else:
        print("invalid operator")

except ZeroDivisionError:
    print("cannot divided by zero")

except ValueError:
    print("invalid input")



