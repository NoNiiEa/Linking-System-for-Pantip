from src.score import *
from src.word_embedding import phrase_embedding, word_embedding

def test_score_word_to_phrases():
    word = "ไก่ทอด"
    phrases = ['ไก่ทอดแน่ๆรสชาติเข้มข้นแซ่บกำลังดีอันนี้', 'รู้จักไก่KFCแล้วก็กลัวร้าน', 'ลูกผมกินไก่ทอดทั่วไปชิ้นนึง', 'ชอบกินไก่ทอดผู้พันKFC', 'กรอบเนื้อนุ่มเฟรนช์ฟรายด์']

    result = score_word_to_phrases(word, phrases)

    assert isinstance(result, dict)
    