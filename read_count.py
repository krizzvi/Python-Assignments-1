def read_and_count(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
    return {
        "lines": text.count('\n') + 1,
        "words": len(text.split()),
        "characters": len(text)
    }
