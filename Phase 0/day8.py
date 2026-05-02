"""#Mixed problem

s=input("enter something").lower


freq={}

for ch in s:
    if ch in freq:
        freq[ch]+=1 
    else:
        freq[ch]=1
    
print(freq)



s=input("enter string")

freq={}

for ch in s:
    if ch ==" ":
        continue   #skip spaces

ch=ch.lower  # lowercase




#max/min list

num=list(map(int,input("enter").split()))

max=num[0]
min=num[0]
for i in num:
    if i>max:
        max=i
    elif i<min:
        min=i
        

print(max)
print(min)


#proper 

num=list(map(int,input("enter:").split()))

large=num[0]
small=num[0]

for i in num:
    if i > large:
        large=i
    if i<small:
        small=i

print("max:",large)
print("min:",small)



num=list(map(int,input("enter the number").split()))

total=0

for i in num:
    total+=i

print(total)

avarage=total/len(num)

print(avarage)

print(len(num))

#perfect version
# 
#  num = list(map(int, input("Enter numbers: ").split()))

if num:
    total = 0

    for i in num:
        total += i

    average = total / len(num)

    print("Sum:", total)
    print("Count:", len(num))
    print("Average:", average)
else:
    print("No input")




text=input("text:")

rev=""

for i in range(len(text)-1,-1,-1):
    rev+=text[i]

print(rev)
    
"""

a,b=map(int,input("enter the number:").split())

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    return a/b

print(add(a,b))
print(sub(a,b))
print(multi(a,b))
print(divide(a,b))


#example upgrade-a, b = map(int, input("Enter numbers: ").split())
op = input("Enter operation (+ - * /): ")

def add(a,b): return a+b
def sub(a,b): return a-b
def multi(a,b): return a*b
def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if op == "+":
    print(add(a,b))
elif op == "-":
    print(sub(a,b))
elif op == "*":
    print(multi(a,b))
elif op == "/":
    print(divide(a,b))
else:
    print("Invalid operation")

