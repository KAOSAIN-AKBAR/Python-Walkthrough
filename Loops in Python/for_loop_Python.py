cars = ["BMW", "MERCEDES", "TOYOTA", "MITSUBISHI"] # car list
for x in cars:
    print(x)

# using break statement in loop
print("\nPrinting LOOP with a break statement")
for x in cars:
    print(x)
    if x == "TOYOTA":
        break


# using continue statement in loop to skip a value in our output
print("\nPrinting LOOP with a continue statement")
for x in cars:
    if x == "TOYOTA":
        continue
    print(x)

##########################################################################################
# To loop through a set of code a specified number of times, we can use the range() function

print("\n")
for x in range(5): # for x=0, x<5, x++  *** 5 is not included within the output ***
    print(x)

print("\n")
for x in range(2,5):  # for x=2, x<5, x++  *** 5 is not included within the output ***
    print(x)

print("\n")
for x in range(2,10,2):  # for x=2, x<10, x=x+2  *** 10 is not included within the output ***
    print(x)

print("\n")

##########################################################################################
# Nested LOOP

cars = [" BMW", " MERCEDES", " TOYOTA", " MITSUBISHI"] # car list
color = ["RED", "BLUE", "GREEN", "YELLOW"] # color list

for x in color:     # initial loop
    for y in cars:  # nested loop
        print(x,y)

