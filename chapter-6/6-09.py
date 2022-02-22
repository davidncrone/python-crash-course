################
# Exercise 6-9 #
################

# Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.

favorite_places = {
    'athos': ['france', 'paris'],
    'porthos': ['buckingham'],
    'aramis': ['gascony', 'california beach', '683 Meadow Ct Des Plaines, IL, 60016-1132 United States'],
}

friends_fav_place = input("What is your favorite place?")
favorite_places['john'] = [friends_fav_place]

for person, places in favorite_places.items():
    print(f"{person}: ", end='')
    for place in places:
        print(f"{place} ", end='')
    print()
