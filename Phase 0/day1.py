# variables -box that stores value 

x=10
name="pratham"
float=2.3
int=45
is_student=True

print(type(x),type(name),type(float),type(int),type(is_student))


#input/output (most important)

input_name = input("Enter the name:")
print(input_name)
#input always return string by default

#if number needed->convert it ising int 


user_name = input("enter your name : ")
user_age=int(input("enter your age:"))

print("Name:", user_name)
print("age next year:", user_age + 1)



a=int(input("enter a:"))
b=int(input("enter b"))


temp=a
a=b
b=temp

print("After swap:")
print( "a =",a)
print( "b =",b)


# shortcut version of swapping

a=int(input("enter the value of a:"))
b=(input("enter the value of b"))

a,b=b,a

print("after swapping:")

print("a",a)
print("b",b)


# simple calculator

a,b= map(int,input("enter the two number by spacing").split())

print("sum:",a+b)
print("substraction",a-b)
print("product:",a*b)
print("division",a/b)



# celcius -> farenheit

#formula= c*9/5+32

celcius= float(input("enter the temperature in celcius"))

f=(celcius*9/5)+32

print("farenhiet:",f)


#tips=⚠️ IMPORTANT RULE (THIS IS YOUR BLOCK FIX)

"""You said:

“Goal: You should NOT freeze on input/output”

So remember this:

If you freeze, it’s usually because:
you forgot int() conversion
you don’t know what input returns
you are overthinking syntax
Fix mindset:

👉 input() ALWAYS gives string
👉 convert ONLY when needed  """

#1

a,b=map(int,input("enter the two number by spacing:").split())

avarage=a+b/2

print("avarage",avarage)

#2

name,age =input("please enter name and age by spacing:").split()

age=int(age)
print("hello",name,"you are",age,"years old")

#3
radius=int(input("enter the radius of circle:"))
 
area=3.14*radius*2

print(area)