from pythainlp.tokenize import subword_tokenize
from pythainlp.tokenize import word_tokenize
from utils import clean_text
from pythainlp.phayathaibert.core import PartOfSpeechTagger
from pythainlp.word_vector import WordVector
from sklearn.metrics.pairwise import cosine_similarity

def find_cosine_sim(vector1, vector2) -> float:
    
    return cosine_similarity(vector1, vector2)[0][0]

phases = ['ไก่ทอดแน่ๆรสชาติเข้มข้นแซ่บกำลังดีอันนี้', 'รู้จักไก่KFCแล้วก็กลัวร้าน', 'ลูกผมกินไก่ทอดทั่วไปชิ้นนึง', 'ชอบกินไก่ทอดผู้พันKFC', 'กรอบเนื้อนุ่มเฟรนช์ฟรายด์']


wv = WordVector()
phases_vector = {}
for phase in phases:
    phases_vector[phase] = wv.sentence_vectorizer(phase)

query_word = "ไก่ทอด"
query_word_vector = wv.sentence_vectorizer(query_word, use_mean=True)

def scoring(phases_vector, query_vector):
    final_score = 0
    for phase, vector in phases_vector.items():
        current_score = find_cosine_sim(vector, query_vector) * 100
        final_score += current_score
        print(f"{phase}, {current_score}")
    return final_score

print(scoring(phases_vector, query_word_vector))

