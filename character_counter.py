def character_count(s):
    s = s.replace(" ", "")
    return {char: s.count(char) for char in set(s)}
