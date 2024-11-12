# Day 4: Only Floats
# Write a function called only_floats, which has two 
# parameters, a and b, and returns 2 if both arguments are floats, 
# 1 if only one argument is a float, and 0 if neither argument is a 
# float. If you pass (12.1, 23) as an argument, your function should 
# return 1.
# Extra Challenge: Index of the Longest Word
# Write a function called word_index that takes one argument, a list
# of strings, and returns the index of the longest word in the list. If 
# there is no longest word (if all the strings are of the same length), the 
# function should return zero (0). For example, the first list below 
# should return 2.
# words1 = ["Hate", "remorse", "vengeance"]
#  And this list below, should return zero (0)
# words2 = ["Love", "Hate"]

def only_floats(a, b):
    # Check if a and b are floats using isinstance
    is_a_float = isinstance(a, float)
    is_b_float = isinstance(b, float)
    
    # Determine the result based on the conditions
    if is_a_float and is_b_float:
        return 2
    elif is_a_float or is_b_float:
        return 1
    else:
        return 0

print(only_floats(12.1, 23))    # Should return 1
print(only_floats(12.1, 23.4))  # Should return 2
print(only_floats(12, 23))      # Should return 0


def word_index(words):
    # Get the lengths of all words in the list
    lengths = [len(word) for word in words]
    
    # Find the maximum length
    max_length = max(lengths)
    
    # Count how many times the max length appears
    if lengths.count(max_length) > 1:
        return 0  # Return 0 if there's more than one word with max length
    
    # Otherwise, return the index of the word with max length
    return lengths.index(max_length)

words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]

print(word_index(words1))  # Should return 2 (index of "vengeance")
print(word_index(words2))  # Should return 0 (all words are the same length)
