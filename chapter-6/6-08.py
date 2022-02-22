################
# Exercise 6-8 #
################

# Pets: Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.


dog = {'type': 'dog', 'owner': 'ted'}
cat = {'type': 'cat', 'owner': 'i am the owner'}
fish = {'type': 'fish', 'owner': 'darla sherman'}

pets = []
pets.append(dog)
pets.append(cat)
pets.append(fish)

for pet in pets:
    print(f"Type: {pet['type'].title()}")
    print(f"Owner: {pet['owner'].title()}\n")
