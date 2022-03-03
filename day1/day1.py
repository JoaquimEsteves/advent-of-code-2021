from textwrap import dedent
from pathlib import Path
import typing as T

test_input = dedent(
    """\
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
"""
)


def get_input(input_str: T.Iterable[str]) -> T.Generator[int, None, None]:
    yield from (int(line) for line in input_str)


def part_1(input_str: T.Iterable[str]) -> int:
    # Test input, ignore at will
    # lines = get_input(test_input.splitlines())
    lines = get_input(input_str)
    prev: int = next(lines)
    number_of_increases = 0
    for inpt in lines:
        if inpt > prev:
            # print(f"{inpt} > {prev}")
            number_of_increases += 1
        prev = inpt
    return number_of_increases

def part_2(input_str: T.Iterable[str]) -> int:
    # Test input, ignore at will
    # lines = get_input(test_input.splitlines())
    raise NotImplementedError()


if __name__ == "__main__":
    with open(Path(__file__).parent / Path("input.txt")) as f:
        print("-- Part 1 --")
        print(part_1(f))
        print("-- Part 2 --")
        print(part_2(f))
