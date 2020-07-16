import re
import sys

text = input("Text: ")

letter = len(re.findall(r'\w', text)) # regex for letters in a text
word = len(re.findall(r'\S+[^\W]', text)) # regex for finding words in a text
sentence = len(re.findall(r"[\sa-zA-Z-,';]+", text)) # regex for sentences in a text

L = (letter * 100) / word
S = (sentence * 100) / word
index = round((0.0588 * L - 0.296 * S - 15.8)) # Coleman-Liau index

if index <= 1.0:
    print("Before Grade 1")
elif index >= 16.0:
    print("Grade 16+")
elif index >= 1.0 and index <= 16.0:
    print(f"Grade {index}")
