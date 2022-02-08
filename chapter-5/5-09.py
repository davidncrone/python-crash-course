################
# Exercise 5-9 #
################

# No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# •	 If the list is empty, print the message We need to find some users!
# •	 Remove all of the usernames from your list, and make sure the correct
#    message is printed.

usernames = ['admin', 'user', 'reddit-moderator',
             'discord-admin', 'neckbeard_uwu']

del usernames[:]

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        elif user != 'admin':
            print(f"Hello {user}, thank you for logging in again.")
elif not usernames:
    print("We need to find some users!")
