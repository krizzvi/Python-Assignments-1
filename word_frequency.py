def word_frequency(text):
    words = text.lower().split()
    return {word: words.count(word) for word in set(words)}
