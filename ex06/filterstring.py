import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3

        s = sys.argv[1]
        n = int(sys.argv[2])

        assert isinstance(s, str)

        words = s.split()
        result = list(
            ft_filter(lambda word: len(word) > n, words)
        )

        print(result)

    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
