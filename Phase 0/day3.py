#what is loop 

# 👉repeat a task multiple times

"""Instead of:
 print(1)
 print(2)
 print(3)


 you do 
"""

"""🔹

 3. range() explained
Code	Meaning
range(5)	0 → 4
range(1, 6)	1 → 5
range(1, 10, 2)	1,3,5,7,9



for i in range (1,4):
 print(i)
 

for i in range(5):
 print(i)


for i in range(1,10):
 print(i)


for i in range(1,10,3):
  print(i)

"""
#while loop
"""
i=0    step 1 - intialize 
while i <5:  step 2- define range
    print(i)  print
    i+=1   # define jump betn number


for i in range(3):
    try:
        num= int(input("enter the number to find the squares"))
        print("square:",num*num)
    except:
        print("invalid input")




n=int(input("enter the numers:"))   #if n= 5

total=0
for i in range(n):  #for in in range(5)
    num=int(input("enter the numbers:"))  # number to addd
    total +=num   #0+num   exam -0+4+4+4
print(total)


#
num=list(map(int,input("enter the numbers#").split()))
print(sum(num))
    


n= int(input("enter the total numbers to calculate"))

add=0
for i in range(n):

    nums=int(input("enter the nums:"))
    add+=nums

print(add)



n = int(input("Enter how many numbers: "))

total = 0

for i in range(n):
    num = int(input("Enter number: "))
    total += num

print("Sum:", total)

"""

"""n=(int(input("take the number from user")))

for i in range(1,11):
 print(f"{n} x {i} = {n*i}")
 print(n,"x",i)=={n*i}
"""

"""n=int(input("enter value of n:"))  #how many time loop will execute to take numbers from users -one by one

total = 0   #to add in other numbers from user

for i in range(n):    # IF WE INPUT 5 AS N THEN RANGE IS 5 SO 5 TIMES LOOP WILL ITERATE
    nums=int(input("enter the one NUMBER at a time"))  #TAKING NUMBERS FROM USERS TO CALCULATE
    total+=nums       # 0+5+5+6+2+9
print("sum",total) #27


num=int(input("enter the number:"))

for i in range(1,11):
   
    table=num*i
    print(num,"*",i,"=",table)


#factorial

n=int(input("enter the number:"))

count=1

for i in range(1,n+1):
    count*=i
print("factorial:",count)




# step 1- take a input number from user
n=int(input("enter the number"))

#set the counter

count=1


# appply for loop where itrate i and print in same line

for i in range(n,0,-1):
    count*=i
    print(i,end="")



#apply condition to prevent extra * at the end

    if i != 1:
        print("*",end="")

# print cal 
print("=",count)



num=input("enter the numbers").split()


n=[int(x) for x in num]

even_count=0

for i in n:
    if i % 2== 0:
        even_count += 1

print("total even numbers:",even_count)



num=int(input("enter the numbers"))   # 10


for i in range(num,0,-1):    # 10,
    print(i," ",end="")



#find largest among n numnbers

n=int(input("enter the number"))

largest=0

for i in range(n):

    num=int(input("enter the number"))
    if num>=largest:
        largest=num
print("the largest number is:",largest)


"""

#break vs continue

#break->👉 i am done ,exit immediately


for i in range(5):
    if i ==3:
        break
    print(i)

for i in range(5):
    if i ==2:
        continue
    print(i)


num=[2,5,8,10]
for i in num:
    if i==8:
        print("found")
        break


for i in range(-3,4):
    if i>=0:
        continue
    print(i)