import random

def scramble_word(word):
    """Scramble the letters of a word"""
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

# Example usage:
word = "python"
scrambled_word = scramble_word(word)
print(f"Original word: {word}")
print(f"Scrambled word: {scrambled_word}")
