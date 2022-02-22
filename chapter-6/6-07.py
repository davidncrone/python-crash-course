################
# Exercise 6-7 #
################

# People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

north_pole_exec_manager = {
    'first_name': 'Santa',
    'last_name': 'Claus',
    'age': 'Unknown',
    'city': 'North Pole'
}

formal_assistant = {
    'first_name': 'Elf',
    'last_name': 'Elferson',
    'age': 'Unknown',
    'city': 'North Pole Local Igloo'
}

commercial_sled_driver = {
    'first_name': 'Rodulph',
    'last_name': 'Red Nosed Reindeer',
    'age': 'Unknown',
    'city': 'North Pole Shed'
}

people = [north_pole_exec_manager, formal_assistant, commercial_sled_driver]

for person in people:
    print("Employee")
    print("________")
    print(f"{person['first_name']}")
    print(f"{person['last_name']}")
    print(f"{person['age']}")
    print(f"{person['city']}")
    print()
