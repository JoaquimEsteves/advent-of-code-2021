"""
Remember to run as a module:
    python3 -m day3.day3

"""
from day1.day1 import uses_input
from textwrap import dedent
import io
import typing as T

# Results
# Part 1: 10100 (22) * 01001 (9) = 198
test_input = dedent(
    """\
    00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010\
"""
)


def bit_not(n, numbits=5):
    """
    One's complement

    ```python
    >>> bin(bit_not(int("10110", 2)))
    '0b1001'
    ```

    The maths behind is is thus (using bitwise subtraction):

    ```python
    >>> int("10110", 2) ^ int("11111", 2)
    9
    ```

    But, when we don't know the number of bits it gets trickier.
    So we shift a 1 N times to the left and then subtract 1
    To get the desired length! Boom, trick solved :)
    """
    return n ^ (1 << numbits) - 1


@uses_input
def part_1(lines: io.TextIOWrapper) -> int:
    """
    I wanted to do something cute and transverse by file by colmun and not
    by row, but I couldn't figure out how to do that.
    So cock it, we just put everything in memory

    Solution: 2035764
    """
    most_common = []

    for column in zip(*lines):
        if column[0] == "\n":
            continue
        ones = 0
        for char in column:
            if char == "1":
                ones += 1
        # Assume no odd numbered column
        # Otherwise we wouldn't have a most common
        if ones > len(column) / 2:
            most_common.append("1")
        else:
            most_common.append("0")

    epsilon, numbits = int("".join(most_common), 2), len(most_common)
    return epsilon * bit_not(epsilon, numbits)


@uses_input
def part_2(_: io.TextIOWrapper) -> int:
    return 0


if __name__ == "__main__":
    print("-- Part 1 --")
    print(part_1())
    print("-- Part 2 --")
    print(part_2())
