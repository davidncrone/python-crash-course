################
# Exercise 3-7 #
################

# Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# •	 Start with your program from Exercise 3-6. Add a new line that prints a
#    message saying that you can invite only two people for dinner.
# •	 Use pop() to remove guests from your list one at a time until only two
#    names remain in your list. Each time you pop a name from your list, print
#    a message to that person letting them know you’re sorry you can’t invite
#    them to dinner.
# •	 Print a message to each of the two people still on your list, letting them
#    know they’re still invited.
# •	 Use del to remove the last two names from your list, so you have an empty
#    list. Print your list to make sure you actually have an empty list at the end
#    of your program

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

del dinner_attendees[0]
del dinner_attendees[0]

print(f"There are {len(dinner_attendees)} people left in the invite list.")
