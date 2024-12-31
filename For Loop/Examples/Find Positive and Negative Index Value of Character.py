### Find the positive and negative index value of 'U' in the following string: str = "PES University"###

str2 = "PES University"

index = str2.index("U")
print(index)
# Output: 4

for i in range(len(str2)):
           if str2[i] == "U":
               positive_index = index
               negative_index = index - len(str2)
               print ("Negative index: ", negative_index)

# Output: Negative index: -10

