# Split Method
# The split() method splits a string into a list.

# splitting with empty separator
problem1 = "Hello my name is Nafi"  # we have a string here
print(problem1)
l1 = problem1.split()  # if we do not specify the separator then by default whitespace is considered as separator
print(l1)  # therefore, each words become item of the list

print()

# splitting by providing separator
problem2 = "Nafi, DT, NSU, UIU"  # we have a string here
print(problem2)
l2 = problem2.split(", ")  # here, we specified the separator so each component before and after ", " will be an item
print(l2)  # therefore, each words become item of the list

print()

# using split for limited item on the list
problem3 = "apple#banana#cherry#orange"
l3 = problem3.split("#", 2) # setting the maxsplit parameter to 1, will return a list with 3 elements
print(l3)

