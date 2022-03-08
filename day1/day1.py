from pathlib import Path
from textwrap import dedent
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


def uses_input(
    func: T.Callable[[T.Generator[int, None, None]], int]
) -> T.Callable[[], int]:
    def inner() -> int:
        with open(Path(__file__).parent / Path("input.txt")) as f:
            # test input
            # return func((int(line) for line in test_input.splitlines()))
            return func((int(line) for line in f))

    return inner


@uses_input
def part_1(lines: T.Generator[int, None, None]) -> int:
    prev: int = next(lines)
    number_of_increases = 0
    for inpt in lines:
        if inpt > prev:
            # print(f"{inpt} > {prev}")
            number_of_increases += 1
        prev = inpt
    return number_of_increases


@uses_input
def part_2(lines: T.Generator[int, None, None]) -> int:
    # Test input, ignore at will
    # lines = get_input(test_input.splitlines())
    a, b, c = next(lines), next(lines), next(lines)
    number_of_increases = 0
    for d in lines:
        if sum((b, c, d)) > sum((a, b, c)):
            # print(f"{ sum((b, c, d)) } > { sum((a, b, c)) }")
            number_of_increases += 1
        a, b, c = b, c, d
    return number_of_increases


if __name__ == "__main__":
    print("-- Part 1 --")
    print(part_1())
    print("-- Part 2 --")
    print(part_2())
