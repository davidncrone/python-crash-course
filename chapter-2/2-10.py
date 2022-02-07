#################
# Exercise 2-10 #
#################

# Adding Comments: Choose two of the programs you've written, and add at least one comment to each. If you don't have
# anything specific to write because your programs are too simple at this point, just add your name and the current
# date at the top of each program file. Then write one sentence describing what the program does


# From exercise 2-7 |
# __________________|
# Program prints name with different variations of white space removal

name = "  \t  David   \n  "

print(name)
print(name.lstrip())  # Removes leading white space and tab character
print(name.rstrip())  # Removes trailing white space and new line character
print(name.strip())  # Removes and escaped characters


# From exercise 2-8 |
# __________________|
# Program prints the evaluation of various expressions

print(5+3)
print(10-2)
print(2*4)
print(int(24/3))  # int() to cast returned value into an integer
