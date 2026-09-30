def load_text(file_path):
    """Read text from a file and return it as a string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def clean_text(text):
    """Convert text to lowercase and remove unnecessary whitespace."""
    text = text.lower()
    return " ".join(text.split())


def tokenize(text):
    """Split text into individual words."""
    return text.split()