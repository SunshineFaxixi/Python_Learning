import pandas

# 1. create a dictionary
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
words_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(words_dict)

# 2. create a list of the phonetic code words from a word that the user inputs
input_words = input("Enter the word:").upper()
result = [words_dict[letter] for letter in input_words]
print(result)