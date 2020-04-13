# tuple

# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# similar to lists. list is represented by [] but tuple is represented by ()

# you cannot add or remove elements from tuple

t = (1, 2, 3)
for p in t:
    print(p)

print()

# even iteration is similar to lists
print(t[0])
print()

# tuple is needed in places where security is main concern. for instance credit card information

# Tuples inside List
credit_card_1 = (987789987, "Kaosain Akbar", "Lecturer", "21/09")
credit_card_2 = (987756987, "Samina Hossain", "Student", "05/06")
credit_cards = [credit_card_1, credit_card_2] # showing two credit card information, you can remove the credit cards
                                              # but cannot change information
print(credit_cards)
print()

# Extracting out and printing tuple values

person = ("Nafi", 25, "Pasta")

(name, age, fav_food) = person

print(name)
print(age)
print(fav_food)

print()

#############################################################################
# Unpacking tuples using loop

person1 = ("Nafi", 25, "Pasta")
person2 = ("Nori", 22, "Wedges")

people = [person1, person2]
print("TUPLE EXTRACTION : \n")

for name, age, fav_food in people:
    print(name)
    print(age)
    print(fav_food)
    print()
