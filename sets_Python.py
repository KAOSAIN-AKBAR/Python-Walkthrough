#                 SETS

# A set is a collection which is unordered and un-indexed. In Python sets are written with curly brackets.

# create set
fruits = {"apple", "banana", "mango"}
print(fruits)
print()

# Accessing items in sets cannot be done by indexing.
# Therefore, we can only use loop to access individual items of sets
fruits = {"apple", "banana", "mango"}
for fruit in fruits:
    print(fruit)
print()

# Sets are specially used to reduce duplicates

l1 = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, "abc", "abc", "pqr", "pqr"] # a list having various duplicate items
print(l1)
no_duplicate = set(l1) # converting list into set
print(no_duplicate) # output comes as SET with only unique elements and no duplicates occur

new_list = list(no_duplicate) # converting set with no duplicates back to LISTS
print(new_list)
print()
###############################################################

print("more operations on set available at https://www.w3schools.com/python/python_sets.asp")