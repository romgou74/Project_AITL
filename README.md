# Artificial Intelligence, Technology and the Law research project

## Background/Motivation
The article 7 of the GDPR requires that consent is presented "in an intelligible and easily accessible form ,using clear and plain language" (Regulation (EU) 2016/679, Art. 7). However, despite this legal requirement, there seems to be little empirical work measuring whether cookie consent notices actually meet this standard, and even less examining whether platforms adjust their language based on the literacy level of their expected audience.   
This project addresses that gap through a readability analysis of cookie consent notices accross 50 (?) major platforms, groupes by target audience age category.

## Research Question
Do cookie consent notices adapt their language complexity tot he expected audience of their platform, and do they meet the GDPR requirements of using clear and understandable language?  

## Methods 
We are planning to obtain the platforms based on rankings from existing websites, which can also filter based on targetted audience. If it is not possible to do automatic filtering on those websites, will be grouping the platforms based on available demographic data (such as on statista). Platforms will be grouped into three/four audience categories : general public, youth-oriented, population of older age group (, professional).

The following metrics were computed for each consent notice : 
- Flesch Reading Ease : 0-100, where a higher number means that it is easier to read
- Flesch-Kincaid Grade Level : US school grade level required
- SMOG Index : Years of education required
- Gunning Fog Index : Years of education based on complex words
- Dale-Chall Score : Difficulty based on complex words (scale of 1-10+)
- Difficult words score : Difficulty based on unfamiliar vocabulary
(pre-processing was handled automatically for the above metrics, as we used the python library textstat to compute them)

We also computed the average sentence length (mean number of words per sentence), and a ratio indicating the amount of vague or ambiguous terms in the consent forms.
For these metrics, minimal preprocessing was applied, as to preserve the natural reading of the text. However, HTML tags, trailing and extra whitespace were removed. Line breaks were replaced with periods where no sentence-ending punctuation was present, and text was put at a lower-case (only for the vague words counting). We opted for no lemmatization, stemming or removal of stopwords which would modify the natural flow of the sentences.

## First Results and observations
For the moment, I applied the code on one consent form and obtained the following results : 
```python
Flesch Reading ease : 26.615238095238112
Flesch-Kincaid Grade Level: 14.764021164021162
SMOG Index : 16.18397175987059
Gunning Fox : 17.712169312169312
Dale-Chall : 10.526248148148149
Difficult words : 0.26455026455026454
```
- Flesch Reading ease is quite low, falls in the very difficult category  
- Flesch-Kincaid Grade level translates to a 3rd year university level  
- SMOG Index also shows that the reader needs a postgraduate level reading  
- Gunning fox recommends 17+ years of education  
- Dale-Chall is above a 10, so it shows that the text is essentially of the maximum difficulty  
- Difficult words shows that there are 25% of words are flagged as uncommon/difficult   
So all these tests point to the fact that this consent form is very difficult to read.  
We need to look at benchmark to continue => average EU adult reading level, could also compute newspapers that everyone reads to see what general language people are expecting

and  

 
```python
15.75 # average sentence length
6.0 # amount of vague/ambiguous words avery 100 words
```

The average length here is not too much  
However, 6 out 100 words are ambiguous, which is quite high  
