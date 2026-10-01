import unittest

from text_processing import clean_text, tokenize


class TestTextProcessing(unittest.TestCase):

    def test_clean_text(self):
        text = "  Hello   WORLD\nPython  "

        result = clean_text(text)

        self.assertEqual(result, "hello world python")

    def test_tokenize(self):
        text = "hello world python"

        result = tokenize(text)

        self.assertEqual(result, ["hello", "world", "python"])


if __name__ == "__main__":
    unittest.main()