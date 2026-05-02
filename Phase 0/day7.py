
#what is dictionary-

#stores data as key -> value

#think

#key-label
#value-actual data

data={"name":"pratham","age":22}

#acess

print(data["name"])  #pratham

#error if key not found


print(data["age"])


data={"name":"pratham",}

#add

data["city"]= "nagpur"
data["age"]=22



      
#better loop t

for k,v in data.items():
    print(k,":",v)

