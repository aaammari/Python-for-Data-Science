import sys
import string


def count_text_characters(text: str):
    """
        Count various types of characters in the provided text.
        Args:
            text (str): The text to analyze.
        Returns:
        print: A number of various types of characters.
    """
    upper = lower = punctuation = spaces = digits = 0
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        elif char in string.punctuation:
            punctuation += 1
        if char.isspace():
            spaces += 1
    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def prompt_text() -> str:
    """Request a string from the user when no argument is provided."""
    print("What is the text to count?")
    try:
        user_input = input()
    except EOFError:
        return ""
    return f"{user_input}\n"


def main(argv=None):
    """Entry point for the text-analyzing script."""
    if argv is None:
        argv = sys.argv

    if len(argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    if len(argv) == 2 and argv[1] != "":
        text = argv[1]
    else:
        text = prompt_text()

    count_text_characters(text)


if __name__ == "__main__":
    main()
