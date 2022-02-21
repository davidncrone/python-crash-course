################
# Exercise 6-3 #
################

# Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •	 Think of five programming words you’ve learned about in the previous
#    chapters. Use these words as the keys in your glossary, and store their
#    meanings as values.
# •	 Print each word and its meaning as neatly formatted output. You might
#    print the word followed by a colon and then its meaning, or print the word
#    on one line and then print its meaning indented on a second line. Use the
#    newline character (\n) to insert a blank line between each word-meaning
#    pair in your output.

glossary = {
    'PEP 8': 'Collect of approved python styling guide for best practice',
    'import this': 'Fun easter egg with words of wisdom',
    'List Comprehension': 'Pythonic way of writing for loops',
    'Indentation Error': 'Are semi colons THAT bad ;P',
    'Wait, these are not words...': 'Worst dictionary 2022',
}

print("DICTIONARY 2022: A deep dive into the practice of combining letters to form words with meaning")
print("______________________________________________________________________________________________")

print(f"PEP 8: {glossary['PEP 8']}\n")
print(f"import this: {glossary['import this']}\n")
print(f"List Comprehension: {glossary['List Comprehension']}\n")
print(f"Indenteation Error: {glossary['Indentation Error']}\n")
print(
    f"Wait, these are not words...: {glossary['Wait, these are not words...']}\n")
