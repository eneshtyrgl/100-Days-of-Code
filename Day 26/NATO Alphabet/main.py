import pandas


#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("100 Days of Code/Day 26/NATO Alphabet/nato_phonetic_alphabet.csv")
phonetic_dict= {
    row.letter: row.code
    for (index, row) in data.iterrows()
}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)