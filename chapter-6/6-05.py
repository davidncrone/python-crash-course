################
# Exercise 6-5 #
################

# Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs
#    through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary.

major_rivers = {
    'nile': 'egypt',
    'mississippi': 'minnesota',
    'rio grande': 'colorado',
}

for river, location in major_rivers.items():
    print(f"The {river.title()} runs through {location.title()}.")

for river in major_rivers:
    print(f"River: {river.title()}")

for location in major_rivers.values():
    print(f"Location: {location.title()}")
