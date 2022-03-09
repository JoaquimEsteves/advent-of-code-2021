import { uses_input } from "../day1/day1.mjs";
import { hrtime } from "process";

// eslint-disable-next-line no-unused-vars
const test_input = `\
forward 5
down 5
forward 8
up 3
down 8
forward 2
`;

const DIRECTIONS = {
  up: "up",
  down: "down",
  forward: "forward",
};

const prepare_text = (input) => input.split("\n").map((a) => a.split(" "));

function part_1(text) {
  const { horizontal, vertical } = prepare_text(text).reduce(
    ({ horizontal = 0, vertical = 0 }, [direction, val]) => {
      switch (direction) {
        case DIRECTIONS.up:
          return { vertical: vertical + parseInt(val), horizontal };
        case DIRECTIONS.down:
          return { vertical: vertical - parseInt(val), horizontal };
        case DIRECTIONS.forward:
          return { horizontal: horizontal + parseInt(val), vertical };
        default:
          // ignore weird stuff
          return { horizontal, vertical };
      }
    },
    {}
  );
  return Math.abs(horizontal * vertical);
}
function part_2(text) {
  const { horizontal, depth } = prepare_text(text).reduce(
    ({ horizontal = 0, aim = 0, depth = 0 }, [direction, val]) => {
      const number = parseInt(val);
      switch (direction) {
        case DIRECTIONS.up:
          return { aim: aim + number, horizontal, depth };
        case DIRECTIONS.down:
          return { aim: aim - number, horizontal, depth };
        case DIRECTIONS.forward:
          return {
            horizontal: horizontal + number,
            depth: depth + aim * number,
            aim,
          };
        default:
          // ignore weird stuff
          return { horizontal, aim, depth };
      }
    },
    {}
  );
  return Math.abs(horizontal * depth);
}

/**
 * I'm not sure which is the most readable.
 * This one's faster 'cos it's just a for loop
 */
function part_2_pythonic(text) {
  const inpt = prepare_text(text);
  let depth = 0;
  let horizontal = 0;
  let aim = 0;
  for (const [direction, val] of inpt) {
    const number = parseInt(val);
    switch (direction) {
      case DIRECTIONS.up:
        aim += number;
        break;
      case DIRECTIONS.down:
        aim -= number;
        break;
      case DIRECTIONS.forward:
        horizontal += number;
        depth += aim * number;
    }
  }
  return Math.abs(horizontal * depth);
}

// if name == "main" nodejs ES6 equivalent
// eslint-disable-next-line no-unused-vars
if (import.meta.url === `file://${process.argv[1]}`) {
  const text_input = uses_input(import.meta.url);
  console.log("-- Part 1 --");
  console.log(part_1(text_input));
  console.log("-- Part 2 --");
  const reduce = hrtime.bigint();
  console.log(part_2(text_input));
  const reduceEnd = hrtime.bigint() - reduce;
  console.log("(pythonic version)");
  const pythn = hrtime.bigint();
  console.log(part_2_pythonic(text_input));
  console.log(`\
Reduce time: ${reduceEnd} ns
Pythonic time: ${hrtime.bigint() - pythn} ns`);
}
