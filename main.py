import re
import string

vague_words = [
    # Vague verbs
    "may", "might", "could", "can", "should",
    # Vague quantifiers
    "some", "certain", "various", "several", "many", "few",
    # Vague adjectives
    "appropriate", "relevant", "necessary", "suitable", "reasonable",
    "adequate", "sufficient",
    # Vague nouns/purposes
    "purposes", "interests", "legitimate", "improve", "enhancement",
    # Vague adverbs
    "sometimes", "occasionally", "generally", "typically", "usually"
]

with open("./data/forms.txt", "r") as f:
    text = f.read()

def cleaning_file(file) :
    """Function which 'cleans' up the file containing consent forms.
    Whitespaces, special characters and numbers are removed but punctuation is kept and no lemmatization is done.
    We also make the words case insensitive (removing caps).
    Input : 
        file (str) : file that we want to clean up
    Return : 
        clean_forms : the cleaned up forms"""
 
    file = re.sub(r'<[^>]+>', '', file)  # remove HTML tags
    lst = file.split('\n')
    lst = [re.sub(r'\s+', ' ', line).strip() for line in lst]

    for i in range (len(lst)) :
        if lst[i] and lst[i][-1] != "." :
            lst[i] += "."
    file = " ".join(lst)

    file = re.sub(r'\s+', ' ', file).strip()  # normalize whitespace 
    cleaned = file.lower()
    return cleaned

text = cleaning_file(text)

def sentence_length(file) :

def vague_find(file) :
    count = 0
    text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
    words = text_no_punct.split()
    if words in vague_words :
        count += 1
    return count/len(words)

print(vague_find(text))
