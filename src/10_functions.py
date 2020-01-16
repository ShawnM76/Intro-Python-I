# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)


def is_even(num):
    if num % 2 == 0:
        return True, "Even!"
    else:
        return False, "Odd!"


# Print out "Even!" if the number is even. Otherwise print "Odd"
print(is_even(num))
# YOUR CODE HERE
