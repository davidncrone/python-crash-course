################
# Exercise 4-4 #
################

# One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop
# it by pressing ctrl-C or by closing the output window.)

million = list(range(1, 1000001))

# Don't recommend doing this many prints!
for num in million:
    print(num)
