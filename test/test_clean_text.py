from src.utils import clean_text

def test_clean_text_thai_html():
    raw = "<p>ผมซื้อ iPhone 15 มาใหม่ ๆ แล้วมันร้อนมากตอนเล่น Genshin Impact!!!</p>"
    expected = "ผมซื้อ iPhone 15 มาใหม่ ๆ แล้วมันร้อนมากตอนเล่น Genshin Impact"
    assert clean_text(raw) == expected