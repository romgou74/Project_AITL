import textstat
import re
import sys
import csv


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
