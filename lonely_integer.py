# Given an array of integers, where all elements but one occur twice, find the unique element.
# Using XOR to find the number is cool :)

def lonely_integer(a):
    result = 0
    for num in a:
        result ^= num
    return result

# Example usage:
my_array = [1, 2, 3, 4, 3, 2, 1]
lonely_integer = lonely_integer(my_array)
print("The lonely integer is:", lonely_integer)