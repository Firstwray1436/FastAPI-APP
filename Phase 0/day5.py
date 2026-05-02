# strings

#what is string

s="pratham"


#indexing acesss

s="hello"

print(s[0])  #h
print(s[1])  #e
print(s[-1]) #o
print(s[-2]) #l

# slicing -cut parts

s="hello"

print(s[0:3])  #hell
print(s[1:4])  #ello
print(s[::-1])



# must builld

s= input()

if s=="":
    print("empty string")
else:
   print(s[::-1])



#imp string method

s="hello world"

print(s.lower())
print(s.upper())
print(s.count("e"))
print(s.replace("h","H"))
print(s.replace("e", "sparni"))
print(s.split())


