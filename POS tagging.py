########### POS tagging ############

# To help the machine understand a sentence, we will tell it what each word is.
# For that we use Part Of Speech tagging and Chunking.
# There are eight main parts of speech:
#   nouns, pronouns, adjectives, verbs, adverbs, prepositions, conjunctions and interjections

### What is chunking¶ ###
# "Chunking is a process of extracting phrases from unstructured text.
# Instead of just simple tokens which may not represent the actual meaning of the text,
# its advisable to use phrases such as “South Africa” as a single word instead of ‘South’ and ‘Africa’ separate words."


import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
text = """In ancient Rome, some neighbors live in three adjacent houses. 
In the center is the house of Senex, who lives there with wife Domina, son Hero, and several slaves, 
including head slave Hysterium and the musical's main character Pseudolus."""


# Preprocess the text
doc = nlp(text)
# Create a list of sentence
sentence_spans = list(doc.sents)
# Display SpaCy vizualizer for each sentence
html = displacy.render(sentence_spans, style="dep", page = True)

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)
    print (spacy.explain ("VBZ"))