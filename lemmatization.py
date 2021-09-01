### 3.Lemmatization ###

import nltk
# nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

# # Init the Wordnet Lemmatizer
lemmatizer = WordNetLemmatizer()
# # Lemmatize Single Word
# print(lemmatizer.lemmatize("bats"))
# #> bat
#
# print(lemmatizer.lemmatize("are"))
# #> are
#
# print(lemmatizer.lemmatize("feet"))
# #> foot
#
# import nltk
# nltk.download('punkt')
#
# # Define the sentence to be lemmatized
# sentence = "The striped bats are hanging on their feet for best"
#
# # Tokenize: Split the sentence into words
# word_list = nltk.word_tokenize(sentence)
# print(word_list)
#> ['The', 'striped', 'bats', 'are', 'hanging', 'on', 'their', 'feet', 'for', 'best']

# Lemmatize list of words and join
# lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
# print(lemmatized_output)
#> The striped bat are hanging on their foot for best

# Can you lemmatize this sentence with nltk?

my_sentence = "Those children are playing. this game, those games, I play he plays"
word_list = nltk.word_tokenize(my_sentence)
lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
print(lemmatized_output)
