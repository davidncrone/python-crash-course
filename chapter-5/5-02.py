################
# Exercise 5-2 #
################

# More Conditional Tests: You don’t have to limit the number of tests you
# create to ten. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# •	 Tests for equality and inequality with strings
# •	 Tests using the lower() method
# •	 Numerical tests involving equality and inequality, greater than and
#    less than, greater than or equal to, and less than or equal to
# •	 Tests using the and keyword and the or keyword
# •	 Test whether an item is in a list
# •	 Test whether an item is not in a list

str1 = "Test string"
str2 = "test string"
print(str1 == str2)  # False
print(str1 != str2)  # True
print(str1.lower() == str2)  # True
print(str1 != str2.lower())  # True
print(23 > 3)  # True
print(3 > 23)  # False
print(3 <= 23)  # True
print(3 < 23 and 3 > 23)  # False
print(3 < 23 or 3 > 23)  # True
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 42]
print(42 in nums)  # True
print(11 in nums)  # True
print(42 not in nums)  # False
print(11 not in nums)  # True
