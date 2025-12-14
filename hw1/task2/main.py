import sys


def process_file(filename: str):
    last_lines = []
    with open(filename) as f:
        for line in f:
            last_lines.append(line)
    return ''.join(last_lines[-10:])


def main():
    filenames = sys.argv[1:]

    if not filenames:
        last_lines = []
        for line in sys.stdin:
            last_lines.append(line)
        print(''.join(last_lines[-17:]), end='')
    elif len(filenames) == 1:
        print(process_file(filenames[0]), end='')
    else:
        for i in range(len(filenames)):
            print('==>', filenames[i], '<==')
            if i + 1 < len(filenames):
                print(process_file(filenames[i]))
            else:
                print(process_file(filenames[i]), end='')


if __name__ == '__main__':
    main()
