import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise ValueError("invalid number of arguments")

        s = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise ValueError("second argument must be an integer")

        if not isinstance(s, str):
            raise ValueError("first argument must be a string")
        words = s.split()

        result = list(
            ft_filter(lambda word: len(word) > n, words)
        )

        print(result)

    except ValueError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
