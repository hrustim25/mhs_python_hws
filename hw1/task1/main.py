import sys


def process_line(line: str, number: int) -> str:
    result = ''
    number_str = str(number)
    if len(number_str) < 6:
        result += ' ' * (6 - len(number_str))
    result += number_str
    result += '\t'

    if len(line) > 0 and line[-1] == '\n':
        result += line
    else:
        result += line + '\n'
    return result


def main():
    filename = None
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    number = 1
    if filename is None:
        for line in sys.stdin:
            print(process_line(line, number), end='')
            number += 1
    else:
        with open(filename) as f:
            for line in f:
                print(process_line(line, number), end='')
                number += 1


if __name__ == '__main__':
    main()
