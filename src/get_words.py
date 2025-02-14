import nltk
import json
from nltk.corpus import words
from nltk import pos_tag

# Download required NLTK datasets
nltk.download("words")
nltk.download("averaged_perceptron_tagger")

# Load words and tag their parts of speech
word_list = words.words()
tagged_words = pos_tag(word_list)

# Define POS categories
pos_categories = {
    "noun": ["NN"],
    "nouns": ["NNS"],
    "verb": ["VB", "VBP"],
    "verbed": ["VBD"],
    "verbing": ["VBG"],
    "adj": ["JJ"],
}

# Create categorized word lists
word_bank = {pos: [] for pos in pos_categories.keys()}

for word, pos in tagged_words:
    for category, pos_tags in pos_categories.items():
        if pos in pos_tags:
            word_bank[category].append(word)

# Save to a JSON file
with open("word_bank.json", "w") as f:
    json.dump(word_bank, f, indent=2)

print("Word bank saved to 'word_bank.json'.")
