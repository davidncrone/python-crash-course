################
# Exercise 6-2 #
################

# Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

fav_nums = {}
fav_nums['Larry'] = '3'
fav_nums['Curly'] = 'three'
fav_nums['Moe'] = '3, three, and pi - 0.14159265358979323846264338327950288419716939937510'

print(f"Larry's favorite number is {fav_nums['Larry']}")
print(f"Curly's favorite number is {fav_nums['Curly']}")
print(f"Moe's favorite number is {fav_nums['Moe']}")

fav_nums['User'] = input("\nWhat is your favorite number?")

print(f"User's favorite number is {fav_nums['User']}")
