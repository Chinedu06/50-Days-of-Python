# Day 2: Strings to Integers
# Write a function called convert_add that takes a list of strings 
# as an argument, converts them to integers, and sums the list. 
# For example, ["1", "3", "5"] should be converted to [1, 3, 5] and 
# summed to 9.
# Extra Challenge: Duplicate Names
# Write a function called check_duplicates that takes a list of strings 
# as an argument. The function should check if the list has any
# duplicates. If there are duplicates, the function should return a list of 
# duplicates. If there are no duplicates, the function should return "no 
# duplicates." For example, the list of fruits below should return 
# ["apple", "banana"], and the list of names should return "no 
# duplicates."
# fruits = ['apple', 'orange', 'banana', 'apple', 'banana']
# names = ['Yoda', 'Moses', 'Joshua', 'Mark']


def convert_add(lst):
    int_list = [int(x) for x in lst]
    
    total_sum = sum(int_list)
    
    return total_sum
    
print(convert_add(["1", "3", "5"])) 
def check_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    if duplicates:
        return list(duplicates)
    else:
        return "no duplicates"

fruits = ['apple', 'orange', 'banana', 'apple', 'banana']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

print(check_duplicates(fruits))
print(check_duplicates(names))

