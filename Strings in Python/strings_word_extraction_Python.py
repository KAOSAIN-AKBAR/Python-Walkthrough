
# String Slicing #
b = "Hello, World!"
print(b[2:5])   # output is "llo"; indexing actually starts from 0. Here 5 is exclusive.

b = "Hello, World!"
print(b[-5:-2])  # output is "orl"; negative indexing goes from backwards. -2 is exclusive

##################################################################################

e="hello this is Nafi from Bangladesh"
q = "Nafi" in e    # if Nafi is in e, the output will be true
print(q)           # The search is case sensitive

e="hello this is Nafi from Bangladesh"
q = "gafi" not in e    # if gafi is not in e, the output will be true
print(q)           # The search is case sensitive