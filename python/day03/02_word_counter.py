# 2. Word Counter
def count_vowels_consonants(sentence):
    vowels = "aeiou"
    v_count = sum(1 for ch in sentence.lower() if ch in vowels)
    c_count = sum(1 for ch in sentence.lower() if ch.isalpha() and ch not in vowels)
    word_count = len(sentence.split())
    return v_count, c_count, word_count
print(count_vowels_consonants("Hello World"))