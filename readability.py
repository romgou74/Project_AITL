import textstat
import re
import sys
import csv

"""
Flesch Reading Ease
Flesch-Kincaid Grade Level
Gunning Fog
SMOG Index
Dale-Chall
"""

filename = sys.argv[1]

with open(filename, "r") as f:
    text = f.read()

file = re.sub(r'<[^>]+>', '', text)  # remove HTML tags
lst = file.split('\n')
lst = [re.sub(r'\s+', ' ', line).strip() for line in lst]

for i in range (len(lst)) :
    if lst[i] and lst[i][-1] != "." :
        lst[i] += "."
file = " ".join(lst)

file = re.sub(r'\s+', ' ', file).strip()  # normalize whitespace
cleaned = file.lower()
cleaned = re.sub(r"[^\w\s]", "", cleaned)
cleaned = cleaned.split()

def get_flesch_reading(text):
    return textstat.flesch_reading_ease(text)

def get_flesch_kincaid(text):
    return textstat.flesch_kincaid_grade(text)

def get_smog(text):
    return textstat.smog_index(text)

def get_gunning(text):
    return textstat.gunning_fog(text)

def get_dale(text):
    return textstat.dale_chall_readability_score(text)

def get_difficult(text, cleaned):
    return textstat.difficult_words(text) / len(cleaned)

print(f"Flesch Reading ease : {textstat.flesch_reading_ease(text)}")
print(f"Flesch-Kincaid Grade Level: {textstat.flesch_kincaid_grade(text)}")
print(f"SMOF Index : {textstat.smog_index(text)}")
print(f"Gunning Fox : {textstat.gunning_fog(text)}")
print(f"Dale-Chall : {textstat.dale_chall_readability_score(text)}")
print(f"Difficult words : {textstat.difficult_words(text)/len(cleaned)}")

