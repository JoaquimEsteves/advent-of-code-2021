"""
Remember to run as a module:
    python3 -m day2.day2

Python's still pretty annoying when it comes to this parent module crap
"""
from day1.day1 import uses_input
from textwrap import dedent
import io
import typing as T

test_input = dedent("""\
    forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2
""")

def transform_input(input: io.TextIOWrapper) -> T.Iterable[T.Tuple[str, int]]:
    """
    Transform the input string into a list of ints
    """
    # input = test_input.splitlines()
    for l in input:
        direction, number = l.split()
        yield direction, int(number)

@uses_input
def part_1(lines: io.TextIOWrapper) -> int:
    horizontal = 0
    vertical = 0
    for direction, number in transform_input(lines):
        if direction == 'forward':
            horizontal += number
        elif direction == 'up':
            vertical += number
        elif direction == 'down':
            vertical -= number
    return abs(horizontal * vertical)

@uses_input
def part_2(lines: io.TextIOWrapper) -> int:
    depth = 0
    aim = 0
    horizontal = 0
    for direction, number in transform_input(lines):
        if direction == 'forward':
            horizontal += number
            depth += aim * number
        elif direction == 'up':
            aim += number
        elif direction == 'down':
            aim -= number
    return abs(horizontal * depth)


if __name__ == "__main__":
    print("-- Part 1 --")
    print(part_1())
    print("-- Part 2 --")
    print(part_2())
