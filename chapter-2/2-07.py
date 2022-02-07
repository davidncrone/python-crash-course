################
# Exercise 2-7 #
################

# Stripping Names: Use a variable to represent a person's name, and include some whitespace characters at the beginning
# and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.
#   Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three
# stripping functions, lstrip(), rstrip(), and strip().

name = "  \t  David   \n  "

print(name)
print(name.lstrip())  # Removes leading white space and tab character
print(name.rstrip())  # Removes trailing white space and new line character
# Removes leading and trailing white space and both escaped characters
print(name.strip())
