from sklearn.metrics.pairwise import cosine_similarity
from .word_embedding import *
from .utils import cosine_similarity

def score_word_to_phrases(word: str, phrases: list) -> dict:
    word = word_embedding(word)
    phrases = phrase_embedding(phrases)
    scores = {}
    for phrase, vector in phrases.items():
        current_score = cosine_similarity(word, vector) * 100
        scores[phrase] = current_score

    total_score = 0
    for phrase, score in scores.items():
        total_score += score

    result = scores
    return result