import sys

def is_even(number):
    return number % 2 == 0

def main(argv):
    if len(argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    if len(argv) == 2:
        try:
            number = int(argv[1])
            if is_even(number):
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            print("AssertionError: argument is not an integer")

if __name__ == "__main__":
    main(sys.argv)