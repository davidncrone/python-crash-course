################
# Exercise 4-2 #
################

# Animals: Think of at least three different animals that have a common
# characteristic. Store the names of these animals in a list, and then use
# a for loop to print out the name of each animal.
# •	 Modify your program to print a statement about each animal, such as
#    A dog would make a great pet.
# •	 Add a line at the end of your program stating what these animals have in
#    common. You could print a sentence such as Any of these animals would
#    make a great pet!

aggressive_animals = ['aligators', 'crocodiles', 'cats']

for animals in aggressive_animals:
    print(animals)

print()

for animals in aggressive_animals:
    print(f"{animals.capitalize()} are animals you should worry about.")


print("\nAny of these animals would quickly become your owner.")
