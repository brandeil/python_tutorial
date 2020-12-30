# Tuple : ordered, immutable, allows duplicate elements
# main difference from list is that it cannot be changed after creation
import sys

mytuple = ("Max", 28, "Boston")
mytuple = "Max", 28, "Boston"  # parenthesis are optional
print(mytuple)

#mytuple[0] = "Tim" # gives error,  tuple object does not support item assignment
  
# tuple has many of the same methods as the `list` type
# see list.py    

# Convert tuple to a list
mylst = list(mytuple)
print(mylst)

# Conver list to a tuple
mytuple2 = tuple(mylst)
print(mytuple2)

# tuple can be more efficient than a list
# list has more bytes than a tuple even though it has the same elements
firstlist = [0, 1, 2, "hello", True]
firsttuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(firstlist), 'bytes')
print(sys.getsizeof(firsttuple), 'bytes')