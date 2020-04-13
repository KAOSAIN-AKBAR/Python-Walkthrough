
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