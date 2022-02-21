################
# Exercise 6-4 #
################

# Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.


# add five more Python terms

glossary = {
    'PEP 8': 'Collect of approved python styling guide for best practice',
    'import this': 'Fun easter egg with words of wisdom',
    'List Comprehension': 'Pythonic way of writing for loops',
    'Indentation Error': 'Are semi colons THAT bad ;P',
    'Wait, these are not words...': 'Worst dictionary 2022',
    'add': 'A form of '
}

for word, description in glossary.items():
    print(f"{word}: {description}")
