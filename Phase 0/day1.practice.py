"""#problem 1-double the number
#take integer input and print double its value 

num=int(input("enter the number"))

print(num*2)



# problem 2- Full name formatter- take first name and last name sepretely and print:
#hello,john doe!

name,surname=(input("enter full name by spacing ")).split()

greeting_name=greeting[0]
greeting_surname=greeting[1]"""

"""print(greeting_name,greeting_surname)"""
"""
print("hello",name,surname,"!")


#problem 3- age in days -take age in years and convert it into days 

age=int(input("enter the age in years"))

cal= age*365

print("you are",cal,"days old")


#simple interest calculator

P,R,T=map(int,input("enter the princal,rate and intrest by comma").split(","))

si=(P*R*T)/100

print(si)


#temperature check 

temp=float(input("enter the temperature in c"))

f=(temp*9/5)+32


print("celsius:",temp)
print("farenheit",f)


#take 3 numbers and print their avarage 

nums=list(map(int,input("enter the three numbers by comma").split(",")))

avarage=sum(nums)/len(nums)


print(avarage)
"""""

num=list(map(int,input("enter the number").split()))

print(sum(num))
print(len(num))

a,b,c=num


avarage=(a+b+c)/3

print(avarage)


