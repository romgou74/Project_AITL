import re
import string
import sys

vague_words = [
    # Vague verbs
    "may", "might", "could", "can", "should",
    # Vague quantifiers
    "some", "certain", "various", "several", "many", "few",
    # Vague adjectives
    "appropriate", "relevant", "necessary", "suitable", "reasonable",
    "adequate", "sufficient", "similar", "standard", "personalized",
    "customized", "enhanced", "improved",

    # Vague nouns/purposes
    "purposes", "interests", "legitimate", "improve", "enhancement",
    "insights", "preferences", "experience", "services", "features"

    # Vague data language
    "information", "content", "activity",
    "behavior", "patterns", "usage", "interactions",
    
    # Vague third party language
    "partners", "third parties", "vendors", "providers", "affiliates",
    
    # Vague actions
    "process", "collect", "use", "share", "store", "access",
    "measure", "analyze", "track", "monitor",
    
    # Vague adverbs
    "sometimes", "occasionally", "generally", "typically", "usually",
    "approximately", "substantially",
    
    # Vague timing
    "periodically", "regularly", "occasionally", "temporarily"
]


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


def sentence_length(file) :
    """Function which computes the average sentence length in a consent form
    Input :
        file (str) : consent form that we wish to examine
    Return :
        (int) : average amount of words per sentence in this consent form"""
    sentences = re.split(r'[.!?]', file)
    sentences = [s.strip() for s in sentences if s.strip()]
    count = [len(s.split()) for s in sentences]
    return sum(count)/len(count)


def vague_find(file) :
    """Function which computes the ratio of vague words for every 100 words in a consent form
    Input :
        file (str) : consent form that we wish to examine
    Return :
        (int) : ratio of vague words in that consent form"""
    count = 0
    text_no_punct = file.translate(str.maketrans('', '', string.punctuation))
    words = text_no_punct.split()
    for word in vague_words:
        count += len(re.findall(r'\b' + word + r'\b', text_no_punct))
    return count/len(words)

