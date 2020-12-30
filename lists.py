# Lists: ordered , mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = list()
print(mylist2)

# list can have different data types
mylist3= [5, True, "apple"]
print(mylist3)

# access element by index (start at 0)
item = mylist[0]
print(item)

last_item = mylist[-1] #-1 is the last item
print(last_item)

# iterate over a list with for loop
for i in mylist3:
    print(i)

# check if item exists
if "apple" in mylist3:
    print("yes")   
else:
    print("no")

# check number of elements in a list with len method
print(len(mylist3))

# append items to end of list
mylist3.append("lemon")
print(mylist3)

# insert in specific position
mylist3.insert(1, "blueberry")
print(mylist3)

# remove last item with pop method
item = mylist3.pop()
print(item)
print(mylist3)

#remove specific element with remove method
item = mylist3.remove("blueberry")
print(mylist3)

# remove all elements with clear method
item = mylist2.clear()
print(mylist2)