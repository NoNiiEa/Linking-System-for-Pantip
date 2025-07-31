from src.word_embedding import *
import numpy as np

def test_phase_embedding():
    phrases = ['ไก่ทอดแน่ๆรสชาติเข้มข้นแซ่บกำลังดีอันนี้', 'รู้จักไก่KFCแล้วก็กลัวร้าน', 'ลูกผมกินไก่ทอดทั่วไปชิ้นนึง', 'ชอบกินไก่ทอดผู้พันKFC', 'กรอบเนื้อนุ่มเฟรนช์ฟรายด์']
    result = phrase_embedding(phrases)
    assert isinstance(result, dict), "Output should be a dict"
    assert len(result) == len(phrases), "Should embed all phrases"

def test_word_embedding():
    word = "ไก่ทอด"
    result = word_embedding(word)
    assert isinstance(result, np.ndarray), "Result shoud be numpy array."
    assert result.shape == (1, 300), "Result should have 300 dimention."