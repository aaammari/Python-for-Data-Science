import sys
import string


def count_text_characters(text: str) -> tuple[int, int, int, int, int, int]:
    """Return totals for the formatted output in this exercise."""
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
        if char == " " or char == "\n" or char == "\r":
            spaces += 1
    return len(text), upper, lower, punctuation, spaces, digits



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

    total_chars, upper, lower, punctuation, spaces, digits = count_text_characters(text)
    print(f"The text contains {total_chars} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
