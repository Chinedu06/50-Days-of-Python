# Day 8: Odd and Even
# Write a function called odd_even that has one parameter and takes 
# a list of numbers as an argument. The function returns the difference 
# between the largest even number in the list and the smallest odd
# number in the list. For example, if you pass [1, 2, 4, 6] as an 
# argument, the function should return 6 - 1= 5.
# Extra Challenge: List of Prime Numbers
# Write a function called prime_numbers. This function asks the
# user to enter a number (an integer) as an argument and returns a list 
# of all the prime numbers within its range. For example, if the user 
# enters 10, your code should return [2, 3, 5, 7] as prime numbers.

def odd_even(lst):
    evens = [i for i in lst if i % 2 == 0]
    odds = [i for i in lst if i % 2 != 0]
    return max(evens) - min(odds)
print(odd_even([1, 2, 4, 6]))

def prime_numbers(num):
    primes = []
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

print(prime_numbers(10))

