from pathlib import Path
from textwrap import dedent
import io
import traceback
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

G = T.TypeVar("G")


def uses_input(
    func: T.Callable[[io.TextIOWrapper], G],
) -> T.Callable[[], G]:
    def inner() -> G:
        with open(
            Path(traceback.extract_stack()[-2].filename).parent / Path("input.txt")
        ) as f:
            return func(f)

    return inner


@uses_input
def part_1(IO: io.TextIOWrapper) -> int:
    lines = (int(line) for line in IO)
    prev: int = next(lines)
    number_of_increases = 0
    for inpt in lines:
        if inpt > prev:
            # print(f"{inpt} > {prev}")
            number_of_increases += 1
        prev = inpt
    return number_of_increases


@uses_input
def part_2(IO: io.TextIOWrapper) -> int:
    lines = (int(line) for line in IO)
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
