
### 2.Embedding ###
from flair.embeddings import WordEmbeddings
from flair.data import Sentence

# init embedding
# glove_embedding = WordEmbeddings('glove')
# diffirent model here
# https://github.com/flairNLP/flair/blob/master/resources/docs/embeddings/CLASSIC_WORD_EMBEDDINGS.md

# create sentence.
# sentence = Sentence('The grass is green .')

# embed a sentence using glove.
# glove_embedding.embed(sentence)
# GloVe embeddings are PyTorch vectors of dimensionality 100

# now check out the embedded tokens.
# for token in sentence:
#     print(token)
#     print(token.embedding)

## Stacked Embeddings

# First, instantiate the two embeddings you wish to combine:
from flair.embeddings import WordEmbeddings, FlairEmbeddings

# init standard GloVe embedding
# glove_embedding = WordEmbeddings('glove')

# init Flair forward and backwards embeddings
# flair_embedding_forward = FlairEmbeddings('news-forward')
# flair_embedding_backward = FlairEmbeddings('news-backward')

# Now instantiate the StackedEmbeddings class and pass it a list containing these two embeddings.
from flair.embeddings import StackedEmbeddings

# create a StackedEmbedding object that combines glove and forward/backward flair embeddings
# stacked_embeddings = StackedEmbeddings([
#                                         glove_embedding,
#                                         flair_embedding_forward,
#                                         flair_embedding_backward,
#                                        ])
#That's it! Now just use this embedding like all the other embeddings, i.e. call the embed() method over your sentences.
# sentence = Sentence('The grass is green .')

# just embed a sentence using the StackedEmbedding as you would with any single embedding.
# stacked_embeddings.embed(sentence)

# now check out the embedded tokens.
# for token in sentence:
#     print(token)
#     print(token.embedding)


## Practice embedding ##
# Can you use SpaCy to embed this sentence?
# sentence = "I love learning"
#
# import spacy
#
# nlp = English()
# tokens = nlp(sentence)
#
# for token in tokens:
#     print(token.text, token.has_vector, token.vector_norm, token.is_oov)
"""
What is the shape of each word's vector?
Results:
I False 0.0 True
love False 0.0 True
learning False 0.0 True
"""

# Try with Flair now.
# glove_embedding = WordEmbeddings('glove')
# sentence = Sentence("I love learning")
# glove_embedding.embed(sentence)
# for token in sentence:
#     print(token)
#     print(token.embedding)