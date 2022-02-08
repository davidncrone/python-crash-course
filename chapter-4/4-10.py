#################
# Exercise 4-10 #
#################

# Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# •	 Print the message The first three items in the list are:. Then use a slice to
#    print the first three items from that program’s list.
# •	 Print the message Three items from the middle of the list are:. Use a slice to
#    print three items from the middle of the list.
# •	 Print the message The last three items in the list are:. Use a slice to print the
#    last three items in the list.


# __________________
# From exercise 4-9 |
# __________________|
# Program calculates the first 10 cubes using a comprehension list

cubes = [num**3 for num in range(1, 11)]

for cube in cubes:
    print(cube)

######################################################################

print(f"\nThe first three items in the list are: {cubes[:3]}.")
# element 4, 5, 6 or [Index 3, 4, 5]
print(f"Three items from the middle of the list are: {cubes[3:6]}")
print(f"The last three items in the list are: {cubes[-3:]}")
