def load_text(file_path):
    """Read text from a file and return it as a string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def clean_text(text):
    """Convert text to lowercase and remove unnecessary whitespace."""
    text = text.lower()
    text = " ".join(text.split())

    return text


def tokenize(text):
    """Split text into individual words."""
    return text.split()


def main():
    file_path = "data/sample.txt"

    text = load_text(file_path)
    cleaned_text = clean_text(text)
    words = tokenize(cleaned_text)

    print("Words:")
    print(words)


if __name__ == "__main__":
    main()