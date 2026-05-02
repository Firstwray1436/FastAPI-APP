"""# palindrom check

text=input("enter:")

if text[::-1]==text:
    print("yes")
else:
    print("No")


#Vovel count
s=input()

count=0

for v in s:
    if v in "aeiouAEIOU":
        count+=1
alphabets="a,b,c,d,e,f,g,h,i,j,k,a,e,i,o,u,g,d,s,e,a,e,i,o,u,o,o,o,o,o,o"
print(count)


s="hello world"

word=s.split()
print(word)

reverse=word[::-1]

print(" ".join(reverse))



s = "pratha m 1234"

count_spaces = 0
count_letter = 0
count_digit = 0

for i in s:
    if i == " ":
        count_spaces += 1
    elif i.isdigit():
        count_digit += 1
    elif i.isalpha():
        count_letter += 1

print("Letters:", count_letter)
print("Spaces:", count_spaces)
print("Digits:", count_digit)


s=input(":")
for i in s:
 if s.count(i)==1:
    print(i)
    break
else:
 print("no unique character")

"""
s=input(":")

words= s.split()
print(words)
        
    

