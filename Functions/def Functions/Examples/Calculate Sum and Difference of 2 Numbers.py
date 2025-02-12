### Calculate Sum and Difference of 2 Numbers ###

def calculation(x, y):
    sum = x + y
    if x > y:
        diff = x - y
    else:
        diff = y -x
    return (sum, diff)

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
print (calculation(x, y)) # Output: sum, diff 
