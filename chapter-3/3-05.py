################
# Exercise 3-5 #
################

# Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# •	 Start with your program from Exercise 3-4. Add a print() call at the end
#    of your program stating the name of the guest who can’t make it.
# •	 Modify your list, replacing the name of the guest who can’t make it with
#    the name of the new person you are inviting.
# •	 Print a second set of invitation messages, one for each person who is still
#    in your list.

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
print(f"Unfortunately, {not_attending} can't make it :(.")
