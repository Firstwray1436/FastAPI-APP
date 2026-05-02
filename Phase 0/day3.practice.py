#sum of n numbers
"""

n=int(input("enter the numebers:"))

count=0

for i in range(n):
    num=int(input("enter the numbers:"))
    count +=num
print("sum of n numer is :",count)




#multiplication table

n=int(input("enter the numberr:"))

for i in range(1,11):
    table=n*i
    print(n,"*",i,"=",n*i)




#factorial

n=int(input("enter the number"))

factorial=1
for i in range(n,0,-1):
     factorial*=i
     if i!=1:
        print(i,end="*")
     else:
         print(i,end="")
print("=",factorial)
    
"""

