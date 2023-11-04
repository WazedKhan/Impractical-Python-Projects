"""Find palindromes in a dictionary file."""

import load_dictionary

# get and store list of words from text file in a list
word_list = load_dictionary.load("single_words.txt")
palindrome_list = []

# iter over each word and check if we reverse it dose it match with same order
# [::-1] revers a string by string slicing
for word in word_list:
    # if match then include in the palindrome_list
    if word == word[::-1]:
        palindrome_list.append(word)

print(f"Number of palindrome found: {len(palindrome_list)}")
