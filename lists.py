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

# reverse a list
mylist3.reverse()
print(mylist3)

# sort a list
numberlist = [2 , 7, 3, 2, 5,6 , 11, 5]
print(numberlist)
numberlist.sort()
print(numberlist)

new_list = sorted(mylist)  # won't change the original list

# concat 2 lists with + operator
list1 = ["apple", "bear"]
list2 = ["dinosaur", "rat"]
list3 = list1 + list2
print(sorted(list3))

# slice for access subparts of a list
list_a = [1, 2, 3, 4, 5,6 ,7 ,8,9]
a= list_a[1:5]
print(a)

a=list_a[3:]  # gets everything from index 3 to the end
print(a)

# copy a list
list_orig = ["apple", "banana", "cherry"]
list_copy = list_orig.copy()
list_copy = list(list_orig)
list_copy = list_orig[:]  # [:] gets everything from list
print(list_copy)

# count number of elements in a list
names = ["John", "John", "Roger"]
print(names.count("John"))

# find the index of an item in a list
print(names.index("Roger"))

# unpacking a list
person = "Max", 28, "Boston"
name, age, city = person  # number of elements on left side must match number of elements on right side
print(city)
print(age)

# unpacking a list with a wildcard
letters = ["a", "d", "x", "y", "z", "t"]
i1, *i2, i3 = letters
print(i1)  # "a"
print(i2) # returns list ["d", "x", "y", "z"]
print(i3) # "t"