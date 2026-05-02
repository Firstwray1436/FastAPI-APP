#exception handeliing

"""🧠 1. What is an Exception?

An exception is an error that happens while program is running.

Example:

x = int("abc")


This gives:

ValueError

Because "abc" cannot become integer.


🔥 2. Common Exceptions
ValueError

Happens when value type is wrong.

int("hello")


ZeroDivisionError

Happens when dividing by zero.

10 / 0


except Exception as e:
    print("Something went wrong:", e)

 Use this carefully. Specific errors are better.






try:
    x=int(input("enter x:"))
    y=int(input("enter y:"))

    print(x/y)

except ZeroDivisionError:
    print("cannot be divided by zero")

except ValueError:
    print("invalid input")



try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    op=input("enter operation(+ - */):")

    if op == "+":
        print(a+b)
    elif op=="-":
        print(a-b)
    elif op =="/":
        print(a/b)
    else:
     print("invalid operation")

except ZeroDivisionError:
    print("cannot divided by zero")

except ValueError:
    print("enter valid input")

"""



