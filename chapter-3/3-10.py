#################
# Exercise 3-10 #
#################

# Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages,
# or anything else you’d like. Write a program that creates a list containing
# these items and then uses each function introduced in this chapter at least
# once.

list = ['mountains', 'rivers', 'countries', 'cities', 'languages']

# Immutable methods
list.append("or anything else you\'d like")
print(list[0])
print(list[-1])
print(list)
print(sorted(list))
print(sorted(list, reverse=True))
print(list)

# Mutable methods
list.sort()
print(list)
list.sort(reverse=True)
print(list)

popped_item = list.pop()
print(popped_item)
print(list)

list.remove('countries')
print(list)

del list[1]
print(list)

list.insert(1, "did you think catch the joke before I deleted it?")
print(list)

print(len(list))
