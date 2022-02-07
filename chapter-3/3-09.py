################
# Exercise 3-9 #
################

# Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 42), use len() to print a message indicating the number
# of people you are inviting to dinner.

# __________________
# From exercise 3-4 |
# __________________|

dinner_attendees = ['Ed', 'Edd', 'Eddy']
print("# of attendees: ", len(dinner_attendees))


# __________________
# From exercise 3-5 |
# __________________|

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

print(
    f"Hi {dinner_attendees[0]}, would you like to come over for dinner? I'm making gravy.")
print(
    f"Hi {dinner_attendees[1]}, would you like to come over for dinner? I'm making gravy.")
print(
    f"Hi {dinner_attendees[2]}, would you like to come over for dinner? I'm making gravy.")

print()
print(f"Unfortunately, {not_attending} can't make it :(.\n")

print("# of attendees: ", len(dinner_attendees))


# __________________
# From exercise 3-6 |
# __________________|

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

print("# of attendees: ", len(dinner_attendees))
# __________________
# From exercise 3-7 |
# __________________|

dinner_attendees = ['Ed', 'Edd', 'Eddy']

print(
    f"Hi {dinner_attendees[0]}, would you like to come over for dinner? I'm making gravy.")
print(
    f"Hi {dinner_attendees[1]}, would you like to come over for dinner? I'm making gravy.")
print(
    f"Hi {dinner_attendees[2]}, would you like to come over for dinner? I'm making gravy.\n")

not_attending = dinner_attendees.pop(1)
dinner_attendees.insert(1, "Jonny")
print(f"Unfortunately, {not_attending} can't make it :(.\n")

# Spot filled
print("Updated List")
print(
    f"Hi {dinner_attendees[0]}, Update: I found a bigger dinner table. More spots available now.")
print(
    f"Hi {dinner_attendees[1]}, Update: I found a bigger dinner table. More spots available now.")
print(
    f"Hi {dinner_attendees[2]}, Update: I found a bigger dinner table. More spots available now.\n")

# More spots available
print("Room for 3 more people!\n")
dinner_attendees.insert(0, 'Nazz')
dinner_attendees.insert(int(len(dinner_attendees) // 2), 'Lee')
dinner_attendees.append('May')
print("Updated List")

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
    f"Hi {dinner_attendees[5]}, Please join me for dinner at 123 Peach Creek.\n")

print("Breaking news, can only invite 2 people now.\n")

removed_invites = []
removed_invite = dinner_attendees.pop()
removed_invites.append(removed_invite)
print("Updated List")
print(
    f"I am sorry {removed_invites[0]}, I can't invite you to dinner now.")

removed_invite = dinner_attendees.pop()
removed_invites.append(removed_invite)
print(
    f"I am sorry {removed_invites[1]}, I can't invite you to dinner now.")

removed_invite = dinner_attendees.pop()
removed_invites.append(removed_invite)
print(
    f"I am sorry {removed_invites[2]}, I can't invite you to dinner now.")

removed_invite = dinner_attendees.pop()
removed_invites.append(removed_invite)
print(
    f"I am sorry {removed_invites[3]}, I can't invite you to dinner now.")

print(f"{dinner_attendees[0]}, you are still invited")
print(f"{dinner_attendees[1]}, you are still invited")

# del dinner_attendees[0]
# del dinner_attendees[0]

print(f"There are {len(dinner_attendees)} people left in the invite list.")

print("# of attendees: ", len(dinner_attendees))
