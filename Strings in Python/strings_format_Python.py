# Changing string to UPPERCASE or lowercase
d = "hEllo WoRld"
print(d)  # output : "hEllo WoRld"
print(d.lower())  # output : "hello world"
print(d.upper())  # output : "HELLO WORLD"

##################################################################################

# Using strip() ----> it removes the white space from beginning and end of the provided string
c = "  Hello World !   "
print(c.strip())  # output : "Hello World !"  ; whitespace is removed from the start and end of the string

##################################################################################

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
item = 567
price = 49.95
order = "I want {} pieces of item {} for {} dollars." # all the {}s are filled with value stated in the print
print(order.format(quantity, item, price))