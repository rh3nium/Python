### Swap 2 numbers ###

def swap_numbers(a, b):
    # Print values before swapping
    print("Before swapping:")
    print("a =", a)
    print("b =", b)

    # Swap using a temporary variable
    temp = a
    a = b
    b = temp

    # Print values after swapping
    print("\nAfter swapping:")
    print("a =", a)
    print("b =", b)

swap_numbers(5, 10)

''' Output:
Before swapping:
a = 5
b = 10

After swapping:
a = 10
b = 5
'''
