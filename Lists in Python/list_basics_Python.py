l1 = [1, 2, 3]  # basic list with integers
print(l1)
print()

l2 = [1, 4.2, True, "hello", [1, 2, 4], l1]  # list with various types of data, even there is another list wintin
print(l2)
print()

# printing items in list using FOR LOOP
print("Print List Items using 'for loop'")
print(l1)
for items in l1:
    print(items)
print()

print(l2)
for items in l2:
    print(items)
print()


# indexing in list ;  indexing starts from 0
print(l2[0])
print(l2[4])
print()