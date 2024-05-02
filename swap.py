def swap_values(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Example usage
x = 5
y = 10
x, y = swap_values(x, y)
print("x =", x)
print("y =", y)
