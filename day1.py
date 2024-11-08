# Write a function called divide_or_square that takes one argument
# (a number) and returns the square root of the number if it is divisible
# by 5, or its remainder if it is not divisible by 5. For example, if you pass
# 10 as an argument, then your function should return 3.16 as the square
# root.

# Extra Challenge: Longest Value
# Write a function called longest_value that takes a dictionary as an
# argument and returns the first longest value of the dictionary. For
# example, the following dictionary should return "apple" as the longest
# value.
# fruits = {'fruit': 'apple', 'color': 'green'}

# Challenge 1: Divide or Square

def divide_or_square(num):
    if num % 5 ==0:
        root = num ** 0.5
        return f'The square root of the number is {root}'
    else:
        remainder = num % 5
        return f'The remainder of the number is {remainder}'

print(divide_or_square(80))
print(divide_or_square(17))

# Extra challenge: Longest Value

def longest_value(d: dict):
    longest = max(d.values(), key=len)
    return longest

fruits = {'fruit': 'apple', 'color': 'green'}
print(longest_value(fruits))
