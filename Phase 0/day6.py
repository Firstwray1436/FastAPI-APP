#list-stores multiple values

l=[1,3,4,5]  #list

l1=["apple",1,333,"banana"]  #list with string and numers

print(l1[-2])  # 333   #indexing


#modify list

l1[1]=10

l1[3]="mango"      #replaced banana with mango

print(l1)

#pop method remove last or index

l1.pop()   #remves banana
l1.pop(2)  #removes 333


print(l1)


##add one numbes using list method

nums=[1,2,4,6]

nums.append(7)  #add on -[1,2,3,4,6]

print(nums)


#user input list 

num1=[int(x) for x in input("enter the number").split()]


num1.append(9)

print(num1)

