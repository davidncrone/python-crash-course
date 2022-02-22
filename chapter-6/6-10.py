#################
# Exercise 6-10 #
#################

# Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
# so each person can have more than one favorite number. Then print
# each person’s name along with their favorite numbers.

fav_nums = {}
fav_nums['Larry'] = '3'
fav_nums['Curly'] = 'three'
fav_nums['Moe'] = '3, three, and pi - 0.14159265358979323846264338327950288419716939937510'

print(f"Larry's favorite number is {fav_nums['Larry']}")
print(f"Curly's favorite number is {fav_nums['Curly']}")
print(f"Moe's favorite number is {fav_nums['Moe']}")

fav_nums['User'] = input("\nWhat is your favorite number?")

print(f"User's favorite number is {fav_nums['User']}")
