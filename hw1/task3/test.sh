#!/bin/bash

echo "Testing reading from file"

for f in tests/test_*.txt; do
    echo "Test $f:"
    diff -s -q <(python3 main.py "$f") <(wc "$f")
done

echo
echo "Testing reading from console"

for f in tests/test_*.txt; do
    echo "Test $f:"
    diff -s -q <(cat "$f" | python3 main.py) <(cat "$f" | wc)
done

echo
echo "Testing multiple files"

diff -s -q <(python3 main.py tests/test_smoke.txt tests/test_new_lines.txt) <(wc tests/test_smoke.txt tests/test_new_lines.txt)

diff -s -q <(python3 main.py tests/test_empty.txt tests/test_no_new_line.txt tests/test_symbols.txt) <(wc tests/test_empty.txt tests/test_no_new_line.txt tests/test_symbols.txt)
