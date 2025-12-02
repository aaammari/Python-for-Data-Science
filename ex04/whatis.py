import sys

def main(argv):
    if len(argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    if len(argv) == 2:
        input_string = argv[1]
        
        if not input_string.lstrip('+-').isdigit():
            print("AssertionError: argument is not an integer")
            return
        number = int(input_string)
        if number % 2 != 0:
            print("I'm Odd.")
            return
        print("I'm Even.")

if __name__ == "__main__":
    main(sys.argv)