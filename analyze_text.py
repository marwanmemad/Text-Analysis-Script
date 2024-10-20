def analyze_text(text):
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    return num_words, num_chars

# مثال على الاستخدام
text = "أهلا بك في عالم البرمجة ببايثون!"
words, chars = analyze_text(text)
print(f"عدد الكلمات: {words}")
print(f"عدد الحروف: {chars}")
