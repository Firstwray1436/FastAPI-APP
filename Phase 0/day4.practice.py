"""
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return a/b

add(5,3)


print(add(4,5))
print(sub(5,7))
print(mul(10,9))
print(divide(2,9))


def facto():
    num=int(input("enter the number"))
    total=1
    for i in range(num,0,-1):
        total*=i
        if i!=1:
            print(i,end="*")
        else:
            print(i,end="")
    print(f"={total}")

facto() 


# max of 3 numbers

a,b,c=map(int,input("enter the number:").split())
def max():
        if a>b and a>c:
            print(a)
        elif b>a and b>c:
            print(b)
        else:
            print(c)

max()




def is_even():      #function declaration
    num=int(input("enter the number"))  #input from user to check the number
    return str(num%2==0).lower()  # str since we cant aplply loweer on bool

    
        
print(is_even())  # print the output in true or false



#sum of list

def total():
    numbers = list(map(int,input("enter the list").split()))
    return(sum(numbers))

print(total())



def prime():
    num=int(input("enter the numbers:"))
    if num<2:
        return("not prime numbers")
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
         return "not prime numbers"
    return("prime number")

print(prime())

"""

