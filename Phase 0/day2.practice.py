"""#take a number and print -positve,negative,zero

num=int(input("enter the number:"))

if num>0:
    print("positive")
elif num<0:
    print("negative")
elif num==0:
    print("zero")

#even and divisible by 3

num=int(input("enter the numer"))

if num % 2 ==0 and num %3==0:
    print("good number")
else:
    print("not good number try different")


#largest of 2 numbers

a,b=map(int,input("enter the number").split())

print(max(a,b))X


#problem 4 - leap year check

year=int(input("enter the year"))

if year % 4==0:
    print(year,"is a leap year")
else:
    print("not leap year")


#problem 5-salary bonus

income=int(input("enter monthly income"))

if income>=50000:
    print("high salary")
elif income<=49999 and income>=20000:
    print("medium salary")
elif income<=20000:
    print("low salary")

"""

a,b,c=map(int,input("enter the numbers").split())     

if (a>=b and a<=c) or (a>=c and a<=b):
    print(a)
elif (b>=a and b<=c) or (b>=c and b<=a):
    print(b)
else:
    print(c)

#pro trick 
a, b, c = map(int, input().split())

if (a - b) * (a - c) <= 0:
    print(a)
elif (b - a) * (b - c) <= 0:
    print(b)
else:
    print(c)