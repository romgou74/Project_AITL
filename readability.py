import textstat

"""
Flesch Reading Ease
Flesch-Kincaid Grade Level
Gunning Fog
SMOG Index
Dale-Chall
"""

with open("./data/forms.txt", "r") as f:
    text = f.read()

print(f"Flesch Reading ease : {textstat.flesch_reading_ease(text)}")
print(f"Flesch-Kincaid Grade Level: {textstat.flesch_kincaid_grade(text)}")
print(f"SMOF Index : {textstat.smog_index(text)}")
print(f"Gunning Fox : {textstat.gunning_fog(text)}")
print(f"Dale-Chall : {textstat.dale_chall_readability_score(text)}")
print(f"Difficult words : {textstat.difficult_words(text)}")
