"""#max in list

num=[int(x) for x in input("enter the numer:").split()]   # input list from user

count=num[0]   #assuming if num[0] is the largest
for i in num:   
    if i>count:   # i>0 then count value be i 
        count=i

print(count)

# find the minimum( same logic)

num=[ int(x) for x  in input("enter:").split()]

min=num[0]

for i in num:
    if i<min:
        min=i


print(min)



num=[int(x) for x in input("enter the numbers").split()]

count=0

for i in num:
    if i>0:
     count +=i

print(count)


# take a input from user
num=[int(x) for x in input("enter the list to reverse it:").split()]

reversed_num=[]   # empty list to store a list in reverse order

for i in range(len(num)-1,-1,-1):          #len(num) gives total length but indexing start from 0 hence range(len(num)-1,)
    
    reversed_num.append(num[i])                                                                          #range(final limit,last(-1 includes last element),jump(-1))

print(reversed_num)

#Pro-tip: You can also do this without a new list by swapping the first and last elements, then the second and second-to-last! 


#find element

num=[int(x)for x in input("enter:").split()]

#ask for search target once:

target=int(input("enter the number to be find"))

found=False  #A flag to track if we find it


# 2 loop throgh the list

for i in num:
    if i== target:
        found= True
        break  #EXIST THE LOOP EARLY ONCE FOUND

#PRINT THE RESULT AFTER CHECKING EVERYTHING

if found:
    print("found")

else:
    print("not found")

"""

#2nd largest in list

num=[int(x) for x in input("enter:").split()]

largest=-float('inf')
second_largest=-float('inf')

for n in num:
    if n>largest:
        second_largest=largest
        largest=n
    elif n> second_largest and n!=largest:
     second_largest=n

print(second_largest)


#improvement -

num = list(map(int, input().split()))

largest = second_largest = float('-inf')

for n in num:
    if n > largest:
        second_largest = largest
        largest = n
    elif largest > n > second_largest:
        second_largest = n

if second_largest == float('-inf'):
    print("No second largest")
else:
    print(second_largest)










