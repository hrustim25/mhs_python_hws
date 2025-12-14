#!/bin/bash

echo "Testing reading from file"

for f in tests/test_*.txt; do
    echo "Test $f:"
    diff -s -q <(python3 main.py "$f") <(tail "$f")
done

echo
echo "Testing reading from console"

for f in tests/test_*.txt; do
    echo "Test $f:"
    diff -s -q <(cat "$f" | python3 main.py) <(cat "$f" | tail -n 17)
done

echo
echo "Testing multiple files"

diff -s -q <(python3 main.py tests/test_smoke.txt tests/test_new_lines.txt) <(tail tests/test_smoke.txt tests/test_new_lines.txt)

diff -s -q <(python3 main.py tests/test_empty.txt tests/test_no_new_line.txt tests/test_cut.txt) <(tail tests/test_empty.txt tests/test_no_new_line.txt tests/test_cut.txt)
