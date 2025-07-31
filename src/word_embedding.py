from pythainlp.word_vector import WordVector
from .utils import clean_text

wv = WordVector()

def phrase_embedding(phrases):
    result = {}
    for phrase in phrases:
        result[phrase] = wv.sentence_vectorizer(phrase)
    return result

def word_embedding(word):
    word = clean_text(word)
    return wv.sentence_vectorizer(word)
