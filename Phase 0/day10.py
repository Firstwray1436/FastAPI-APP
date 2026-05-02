"""try:
    n=int(input("enter number:"))
    
    if n<0:
        print("factorail not defined for negative numbers")
    else:
        factorial=1
        for i in range(n,0,-1):
            factorial*=i
    
    print("factorial:",factorial)

except ValueError:
    print("enter only numbers")


text=input("enter text:")

if text.strip()=="":
    print("empty input")
else:
    cleaned=text.replace(" ","").lower()

if cleaned == cleaned[::-1]:
    print("palindrome")
else:
    print("not palindrome")



text=input("enter task:")

if text.strip()=="":
    print("empty input")

else:
    freq={}

for ch in text:
    if ch == " ":
        continue
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

print(freq)


l=list(map(int,input("enter the number:").split()))

if l.strip()=="":
 print("empty input")

  

 maaximum=l[0]
 minimum=l[0]
 try:
     if len(l)==0:
      print("empty")
     else:
      for m in l:
       if m > maaximum:
        maaximum=m
      if m<minimum:
        minimum=m


     print(maaximum)
     print(minimum)
 except ValueError:
  print("enter valid numbers")
"""


try:
    a=int(input("enter the numbers"))
    b=int(input("enter the numbers"))
    op=input("enter operation sign to perform")

    if op== "-":
        print(a-b)
    elif op=="+":
        print(a+b)
    elif op=="/":
        print(a/b)
except ZeroDivisionError:
    print("cannot divide bu zero")
except ValueError:
    print("wrong input")

#better version-
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        print("Result:", a + b)

    elif op == "-":
        print("Result:", a - b)

    elif op == "*":
        print("Result:", a * b)

    elif op == "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a / b)

    else:
        print("Invalid operator")

except ValueError:
    print("Enter valid numbers only")

