################
# Exercise 3-6 #
################

# More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
#    call to the end of your program informing people that you found a bigger
#    dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in your list.

dinner_attendees = ['Ed', 'Edd', 'Eddy']

print(
    f"Hi {dinner_attendees[0]}, would you like to come over for dinner? I'm making gravy.")
print(
    f"Hi {dinner_attendees[1]}, would you like to come over for dinner? I'm making gravy.")
print(
    f"Hi {dinner_attendees[2]}, would you like to come over for dinner? I'm making gravy.")
print()

not_attending = dinner_attendees.pop(1)
dinner_attendees.insert(1, "Jonny")
print(f"Unfortunately, {not_attending} can't make it :(.")
print()

# Spot filled
print(
    f"Hi {dinner_attendees[0]}, Update: I found a bigger dinner table. More spots available now.")
print(
    f"Hi {dinner_attendees[1]}, Update: I found a bigger dinner table. More spots available now.")
print(
    f"Hi {dinner_attendees[2]}, Update: I found a bigger dinner table. More spots available now.")

# More spots available
dinner_attendees.insert(0, 'Nazz')
dinner_attendees.insert(int(len(dinner_attendees) // 2), 'Lee')
dinner_attendees.append('May')
print()
print("Final List")

print(
    f"Hi {dinner_attendees[0]}, Please join me for dinner at 123 Peach Creek.")
print(
    f"Hi {dinner_attendees[1]}, Please join me for dinner at 123 Peach Creek.")
print(
    f"Hi {dinner_attendees[2]}, Please join me for dinner at 123 Peach Creek.")
print(
    f"Hi {dinner_attendees[3]}, Please join me for dinner at 123 Peach Creek.")
print(
    f"Hi {dinner_attendees[4]}, Please join me for dinner at 123 Peach Creek.")
print(
    f"Hi {dinner_attendees[5]}, Please join me for dinner at 123 Peach Creek.")
