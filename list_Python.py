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

# add data to predefined list, using append, data is added to last
l3 = ["Nafi", "Nori", "NSU"]  # predefined list, given
print(l3)
l3.append("UIU")
print(l3)
print()

# add data to predefined list, using insert, data is added to desired position
l3 = ["Nafi", "Nori", "NSU"]  # predefined list, given
print(l3)
l3.insert(3, "UIU")  # insert UIU in the third position of the list, first item having index 0
print(l3)
print()

# remove item from the list
l3 = ["Nafi", "Nori", "NSU"]  # predefined list, given
print(l3)
l3.remove("NSU")  # remove NSU from the list and this is CASE-SENSITIVE
print(l3)
print()

# reverse items in the list
l4 = ["Nafi", "Nori", "NSU", "UIU"]  # predefined list, given
print(l4)
l4.reverse()  # this is a stand alone operation and need not required to be placed inside any print function
print(l4)
print()

# sort item in the list
l4 = ["Nafi", "Nori", "NSU", "UIU", "DT"]  # predefined list, given
print(l4)
l4.sort()  # this is a stand alone operation and need not required to be placed inside any print function
print(l4)  # sorting is done alphabetically
print()

l5 = [20, 10, 40, 30, 70, 50, 60]  # predefined list, given
print(l5)
l5.sort()  # this is a stand alone operation and need not required to be placed inside any print function
print(l5)  # sorting is done numerically
print()

###### ******* YOU CANNOT SORT LISTS THAT HAVE MULTIPLE TYPES OF DATA WITHIN THEM ******** ##########
