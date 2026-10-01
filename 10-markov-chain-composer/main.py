from markov import build_markov_chain, generate_text
from text_processing import load_text, clean_text, tokenize


def create_chain(file_path):
    """Load a text file and build a Markov chain from it."""
    text = load_text(file_path)
    cleaned_text = clean_text(text)
    words = tokenize(cleaned_text)

    if len(words) < 3:
        raise ValueError("The source text must contain at least 3 words.")

    return build_markov_chain(words)


def run_program():
    """Run the text generation application."""
    default_file = "data/sample.txt"

    file_path = input(
        f"Source file [{default_file}]: "
    ).strip()

    if not file_path:
        file_path = default_file

    try:
        chain = create_chain(file_path)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        return

    print("\nMarkov Text Composer")
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