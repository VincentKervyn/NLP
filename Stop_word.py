############ Stop word ###########

# Remove all my stop words
text = "At BeCode, we like to learn. Sometime, we play games not win a price but to have fun!"
result = str(['BeCode', ',', 'like', 'learn', '.', ',', 'play', 'games', 'win', 'price', 'fun', '!'])


# You can use any library!
## Using NLTK ##
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(text)
print ("## NLTK ##")
print(word_tokens)

## Using SpaCy ##
from spacy.lang.en import English

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = English()

#  "nlp" Object is used to create documents with linguistic annotations.
my_doc = nlp(text)

# Create list of word tokens
token_list = []
for token in my_doc:
    token_list.append(token.text)

from spacy.lang.en.stop_words import STOP_WORDS

# Create list of word tokens after removing stopwords
filtered_sentence =[]

for word in token_list:
    lexeme = nlp.vocab[word]
    if lexeme.is_stop == False:
        filtered_sentence.append(word)

print ('## SpaCy ##')
print(token_list)
print(filtered_sentence)
#####
print ('The result should be something like this:\n', result)

