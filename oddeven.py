def odd_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Prompt the user to enter a number
number = int(input("Enter a number: "))

result = odd_even(number)
print("The number", number, "is", result)
