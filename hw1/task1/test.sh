#!/bin/bash

# Create big test
echo '' >tests/test_many_lines.txt
for ((i=1; i < 1000001; i++))
do
echo '1' >>tests/test_many_lines.txt
done

echo "Testing reading from file"

for f in tests/test_*.txt; do
    echo "Test $f:"
    diff -s -q <(python3 main.py "$f") <(nl -b a "$f")
done

echo
echo "Testing reading from console"

for f in tests/test_*.txt; do
    echo "Test $f:"
    diff -s -q <(cat "$f" | python3 main.py) <(cat "$f" | nl -b a)
done

# Delete big test
rm tests/test_many_lines.txt
