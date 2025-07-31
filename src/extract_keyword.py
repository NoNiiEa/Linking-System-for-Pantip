import pythainlp
from .utils import clean_text
from pythainlp.tokenize import word_tokenize

text_title = """
ทำไมถึงชอบ กินไก่ทอดผู้พัน กันครับ
 ทำไมถึงชอบกินไก่ทอดผู้พัน KFC กันครับ
  สงสัยตัวเองมาก พยายามงดของทอด แต่ตะบะแตกทุกที ที่ผ่านร้านไก่ทอด KFC

ผมพยายามลดน้ำหนักแล้วนะ พอลดลงมาได้   มันจะมีชีทเดย์ไง  ก็ไปใจแตกกับไก่ทอดร้านนี้ตลอดเลย เมื่อวานนั
ก็เพิ่งโดนไปมาดๆ ครับ   ใครเป็นบ้าง เพราะอะไรเล่าให้ฟังกันบ้างครับ
น่าจะเป็นเพราะกลิ่นหอมเฉพาะตัวของไก่ทอดแน่ๆ
รสชาติเข้มข้น แซ่บกำลังดี อันนี้มีรสเปรี้ยวๆ เผ็ดๆ ต้องดื่มรีฟิวตามเลย ผมเอาสลัดผักไปแกล้มด้วย
ความกรุบกรอบทุกคำที่เคี้ยวหนังไก่
ความเค็มมันลงตัว เนื้อไก่นุ่มมากมีกลิ่นเครื่องเทศถึงข้างใน
ที่สำคัญ กินในร้านมันจะร้อนกำลังดี มีแอร์เย็นเป่านั่งสบายด้วย

ข้อเสียคือ ชิ้นเล็กไปนิด ถ้าไม่ใช่วันอังคาร ก็เกือบหมดตัวเลย

ปล ไปกินที่ญี่ปุ่นไม่ฟินเท่าที่เมืองไทย
"""
text_comment = """
ชอบเพราะหนังไก่กรอบมากกกกค่ะ เรานี่ลอกกินหนังก่อนเลย 5555
มันหากินง่ายด้วยมั้งคะ เดี๋ยวนี้มีน้ำรีฟีลเกือบทุกที่แล้วด้วย เราว่าคุ้ม
ชอบวิ้งแซ่บสุดแล้วกับเฟรนซ์ฟรายค่ะ ไก่ทอดนี่เราแทบไม่ได้กินละเพราะมันเล็กไม่อิ่ม กินเป็นชุดข้าวกับวิ้งแซ่บอย่างเดียวเลย 
ผมก็ชอบเพราะมันกรอบ เนื้อนุ่ม เฟรนช์ฟรายด์ก็อร่อย โดยเฉพาะมันบดครับ 
อร่อย และของทอดกับเรา มันเหมือนเกิดมาคู่กันอยู่แล้ว
ผมก็ชอบ แต่กินแค่ปีนึง 2-3 ครั้งพอแล้ว
ลูกผมกินไก่ทอดทั่วไป ชิ้นนึงบางทีก็ไม่หมด
ถ้าไก่ผู้พัน 3 ชิ้นไม่เหลือ
อาจจะเป็นรสชาติที่คุ้นเคย  และก็เป็นความเคยชินที่ติดลิ้นมาตั้งแต่รู้จักไก่ KFC 
แล้วก็กลัวร้านเขาอยู่ไม่ได้  ไปเกือบทุกอังคารเลยค่ะ
เวลาไปกินไก่ผู้พันผมจะกินแต่วิ้งแซ่บ ไก่ทอดแบบปกติผมไม่กินเลย
เพราะรสชาติแรง และจัดจ้านดี บวกกับซอสพริกซอสมะเขือเทศ
เอามาเทียบกับไก่ย่างหาดใหญ่ ไก่ทอดของห้าดาว มันก็อร่อยกว่าแน่ๆแต่ที่แพ้คือขนาด 55+
ชอบนักเก็ต + ซอสหวานๆ
ผมกินทีไรนี่เก็บเรียบเลยครับ แม้แต่เศษแป้งทอดที่หลุดจากหนังไก่ และไม่ชอบนั่งกินที่ร้าน จะสั่งมากินที่บ้าน (กลังคนอื่นเห็นว่ากินมูมมาม 555 😁😁😁)
เครื่องปรุงที่หมักในไก่ครับ  hot&spicy เจ้านี้ ยังไม่มีใครทำเหมือนเลย
ผมกินแบบไม่ต้องจิ้มซอสก็อร่อยละครับ
ถ้าอย่างอื่นก็จะเป็นมันบด ที่ทำได้ดีเหมือนกัน
หลานผมก็ชอบนักชอบหนา เจอร้านนี่พลาดไม่ได้ ผมจะช่วยกินก็ยูริคเกิน
"""
def RAKE(title, comment, top_n=5):
    """
    Extract keywords from Thai text using a RAKE(Rapid Automatic Keyword Extraction).
    Using title and comment text
    with title weight = 1 and comment weight = 0.7
    """
    title_clean = clean_text(title)
    comment_clean = clean_text(comment)
    title_tokens = word_tokenize(title_clean, engine='newmm', keep_whitespace=False)
    comment_tokens = word_tokenize(comment_clean, engine='newmm', keep_whitespace=False)
    tokens = title_tokens + comment_tokens
    
    stop_words = pythainlp.corpus.thai_stopwords()
    phases = []
    current_phase = []
    
    for token in tokens:
        if token not in stop_words:
            current_phase.append(token)
        else:
            if len(current_phase) > 0:
                phases.append(current_phase)
            current_phase = []

    degree = {}
    for token in tokens:
        for phase in phases:
            if token in phase:
                if token not in degree:
                    degree[token] = 0
                degree[token] += len(phase) - 1

    
    freq = {}
    for token in tokens:
        for phase in phases:
            for word in phase:
                if token == word:
                    if token not in freq:
                        freq[token] = 0
                    freq[token] += 1
    
    score = {}
    for phase in phases:
        current_score = 0
        for word in phase:
            k = 1 if word in title_tokens else 0.7
            current_score += (degree.get(word, 0) / freq.get(word, 0)) * k
        score["".join(phase)] = current_score
    
    sorted_score = sorted(score.items(), key=lambda x: x[1], reverse=True)
    return [keyword for keyword, _ in sorted_score[:top_n]]

if __name__ == "__main__":
    print(RAKE(title=text_title, comment=text_comment, top_n=5))




