#################
# Exercise 5-10 #
#################

# Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# •	 Make a list of five or more usernames called current_users.
# •	 Make another list of five usernames called new_users. Make sure one or
#    two of the new usernames are also in the current_users list.
# •	 Loop through the new_users list to see if each new username has already
#    been used. If it has, print a message that the person will need to enter a
#    new username. If a username has not been used, print a message saying
#    that the username is available.
# •	 Make sure your comparison is case insensitive. If 'John' has been used,
#    'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
#    current_users containing the lowercase versions of all existing users.)

current_users = ['admin', 'user', 'reddit-moderator',
                 'discord-admin', 'neckbeard_uwu']

current_users_lowercase = []

for user in current_users:
    current_users_lowercase.append(user.lower())

new_users = ['Bom Trady', 'Jaden Sniff',
             'reddit-moderator', 'Kanye East', 'neckbeard_uwu']

if new_users:
    for new in new_users:
        if new.lower() in current_users_lowercase:
            print(f"username: {new} is already taken, please choose another.")
        elif new not in current_users_lowercase:
            print(f"username: {new} is available.")
