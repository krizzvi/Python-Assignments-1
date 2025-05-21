import inflect
def number_to_words(n):
    p = inflect.engine()
    return p.number_to_words(n)
