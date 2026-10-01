import unittest

from markov import build_markov_chain, generate_text


class TestMarkov(unittest.TestCase):

    def test_build_markov_chain(self):
        words = ["the", "cat", "sat", "the", "cat"]

        result = build_markov_chain(words)

        expected = {
            "the": ["cat", "cat"],
            "cat": ["sat"],
            "sat": ["the"],
        }

        self.assertEqual(result, expected)

    def test_generate_text_length(self):
        words = ["the", "cat", "sat", "the", "cat"]
        chain = build_markov_chain(words)

        result = generate_text(chain, 5)

        self.assertEqual(len(result.split()), 5)

    def test_generate_text_invalid_count(self):
        chain = {"hello": ["world"]}

        with self.assertRaises(ValueError):
            generate_text(chain, 0)

    def test_generate_text_empty_chain(self):
        with self.assertRaises(ValueError):
            generate_text({}, 5)


if __name__ == "__main__":
    unittest.main()

    