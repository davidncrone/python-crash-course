#################
# Exercise 4-11 #
#################

# My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# •	 Add a new pizza to the original list.
# •	 Add a different pizza to the list friend_pizzas.
# •	 Prove that you have two separate lists. Print the message My favorite
#    pizzas are:, and then use a for loop to print the first list. Print the message
#    My friend’s favorite pizzas are:, and then use a for loop to print the second list.
#    Make sure each new pizza is stored in the appropriate list.


# __________________
# From exercise 4-1 |
# __________________|
# Program calculates the first 10 cubes using a comprehension list

fav_pizzas = ['pepperoni', 'olive', 'mushroom',
              'linguica', 'anything but pineapple']

for pizza in fav_pizzas:
    print(f"I like {pizza} pizza.")

print("\nI don't like pizza, I don't love pizza, I live for pizza.")

##################################################################

friend_pizzas = fav_pizzas[:]

fav_pizzas.append('cheese')
friend_pizzas.append('anchovies')

# Code below has extra commas at the end as certain features
# have not been explained yet in the book.

print("My favorite pizzas are: ", end='')

for pizza in fav_pizzas:
    print(pizza, end=', ')

print("\nMy friend's favorite pizzas are: ", end='')

for pizza in friend_pizzas:
    print(pizza, end=', ')
