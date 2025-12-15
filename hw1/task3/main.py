import sys


def process_file(filename: str):
    stats = [0, 0, 0]
    with open(filename) as f:
        for line in f:
            stats[0] += (len(line) > 0 and line[-1] == '\n')
            stats[1] += len(line.split())
            stats[2] += len(line)
    return stats + [filename]


def print_stats(stats: list, width: int):
    for i in range(3):
        value_str = str(stats[i])
        result = ''
        if len(value_str) + (i == 0) <= width:
            result += ' ' * (width - len(value_str) - (i == 0))
        else:
            result += ' '
        result += value_str
        print(result, end='')
    if len(stats) == 4:
        print(' ', stats[3], sep='', end='')
    print()


def main():
    filenames = sys.argv[1:]

    if not filenames:
        stats = [0, 0, 0]
        for line in sys.stdin:
            stats[0] += (len(line) > 0 and line[-1] == '\n')
            stats[1] += len(line.split())
            stats[2] += len(line)
        print_stats(stats, 8)
    elif len(filenames) == 1:
        stats = process_file(filenames[0])
        max_len = 0
        for i in range(3):
            max_len = max(max_len, len(str(stats[i])))
        print_stats(stats, max_len+1)
    else:
        total_stats = [0, 0, 0, 'total']
        stats_per_file = []
        max_len = 0
        for filename in filenames:
            stats_per_file.append(process_file(filename))
            for i in range(3):
                max_len = max(max_len, len(str(stats_per_file[-1][i])))
                total_stats[i] += stats_per_file[-1][i]
        for i in range(3):
            max_len = max(max_len, len(str(total_stats[i])))
        for stats in stats_per_file:
            print_stats(stats, max_len+1)
        print_stats(total_stats, max_len+1)


if __name__ == '__main__':
    main()
