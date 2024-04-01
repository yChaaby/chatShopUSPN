import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import FrenchStemmer

stemmer = FrenchStemmer()

def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return word_tokenize(sentence, language='french')


def stem(word):
    """
    stemming = find the root form of the word
    """
    if '-' in word:
        parts = word.split('-')
        stemmed_parts = [stemmer.stem(part.lower()) for part in parts]
        return stemmed_parts
    else:
        return stemmer.stem(word.lower())
    


def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag

def flatten_list(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened