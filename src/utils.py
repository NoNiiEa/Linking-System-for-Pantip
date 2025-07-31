from sklearn.metrics.pairwise import cosine_similarity
import re
import html

def find_cosine_sim(vector1, vector2) -> float:
    return cosine_similarity(vector1, vector2)[0][0]

def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\u0E00-\u0E7F\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text