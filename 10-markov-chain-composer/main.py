from markov import build_markov_chain, generate_text


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


def run_program():
    """Run the text generation application."""
    file_path = "data/sample.txt"

    text = load_text(file_path)
    cleaned_text = clean_text(text)
    words = tokenize(cleaned_text)
    chain = build_markov_chain(words)

    print("Markov Text Composer")
    print("--------------------")

    while True:
        user_input = input(
            "\nHow many words should I generate? (q to quit): "
        ).strip()

        if user_input.lower() == "q":
            print("Goodbye!")
            break

        try:
            word_count = int(user_input)

            if word_count <= 0:
                print("Please enter a positive number.")
                continue

            generated_text = generate_text(chain, word_count)

            print("\nGenerated text:")
            print(generated_text)

        except ValueError:
            print("Please enter a valid number.")


def main():
    run_program()


if __name__ == "__main__":
    main()