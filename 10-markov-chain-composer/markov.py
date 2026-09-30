import random


def build_markov_chain(words):
    """Build a mapping of each word to the words that follow it."""
    chain = {}

    for current_word, next_word in zip(words, words[1:]):
        if current_word not in chain:
            chain[current_word] = []

        chain[current_word].append(next_word)

    return chain


def generate_text(chain, word_count):
    """Generate new text using the Markov chain."""
    if not chain:
        raise ValueError("Cannot generate text from an empty chain.")

    if word_count <= 0:
        raise ValueError("Word count must be greater than 0.")

    current_word = random.choice(list(chain.keys()))
    generated_words = [current_word]

    for _ in range(word_count - 1):
        next_words = chain.get(current_word)

        if not next_words:
            break

        current_word = random.choice(next_words)
        generated_words.append(current_word)

    return " ".join(generated_words)