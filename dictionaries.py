# Dictionary: Key-Value pairs, Unordered, Mutable

# create
mydict = {"name":"Max","age":28,"city":"New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

# access the values
value = mydict["name"]
print(value) # Max

# add key-value to dictionary
mydict["email"] = "max@xyz.com"
print(mydict)

# delete
del mydict["name"]
mydict.pop("age")
mydict.popitem() # removes last key-value

# check if key is in dictionary
if "age" in mydict:
    print(mydict["age"])