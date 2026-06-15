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
    Whitespaces and html tags are removed but punctuation is kept and no lemmatization is done.
    We also make the words case insensitive (removing caps), and add a dot at the end of each
    line where there was only a line break to ensure that different lines are not merged.
    Input : 
        file (str) : file that we want to clean up
    Return : 
        clean_forms (str) : the cleaned up forms"""
 
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
    """Function which computes the average sentence length in a consent form
    Input :
        file (str) : consent form that we wish to examine
    Return :
        (int) : average amount of words per sentence in this consent form"""
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    count = [len(s.split()) for s in sentences]
    return sum(count)/len(count)

print(sentence_length(text))

def vague_find(file) :
    """Function which computes the ratio of vague words for every 100 words in a consent form
    Input :
        file (str) : consent form that we wish to examine
    Return :
        (int) : ratio of vague words in that consent form"""
    count = 0
    text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
    words = text_no_punct.split()
    if words in vague_words :
        count += 1
    return count/len(words)

print(vague_find(text))
