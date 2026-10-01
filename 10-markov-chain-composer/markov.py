import random


def build_markov_chain(words):
    """Build a Markov chain using pairs of consecutive words."""
    chain = {}

    if len(words) < 3:
        return chain

    for first, second, next_word in zip(words, words[1:], words[2:]):
        key = (first, second)

        if key not in chain:
            chain[key] = []

        chain[key].append(next_word)

    return chain


def generate_text(chain, word_count):
    """Generate text using the Markov chain."""
    if not chain:
        raise ValueError("Cannot generate text from an empty chain.")

    if word_count <= 0:
        raise ValueError("Word count must be greater than 0.")

    first, second = random.choice(list(chain.keys()))
    generated_words = [first, second]

    while len(generated_words) < word_count:
        next_words = chain.get((first, second))

        if not next_words:
            break

        next_word = random.choice(next_words)
        generated_words.append(next_word)

        first, second = second, next_word

    return " ".join(generated_words[:word_count])