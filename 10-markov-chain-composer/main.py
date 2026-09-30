def load_text(file_path):
    """Read text from a file and return it as a string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def clean_text(text):
    """Convert text to lowercase and remove unnecessary whitespace."""
    text = text.lower()
    text = " ".join(text.split())

    return text


def main():
    file_path = "data/sample.txt"

    text = load_text(file_path)
    cleaned_text = clean_text(text)

    print("Original text:")
    print(text)

    print("\nCleaned text:")
    print(cleaned_text)


if __name__ == "__main__":
    main()