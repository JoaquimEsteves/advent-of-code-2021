import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

// on ESModule mode we don't have access to __dirname
// So this weirdness is required
// See: https://bobbyhadz.com/blog/javascript-dirname-is-not-defined-in-es-module-scope
// We have to pass the import.meta.url everytime as it depends on location the caller
export const uses_input = (filename = import.meta.url) =>
  fs.readFileSync(
    path.join(path.dirname(fileURLToPath(filename)), "input.txt"),
    "utf8"
  );

// eslint-disable-next-line no-unused-vars
const test_input = `\
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
`;

function part_1(text) {
  const [prev, ...input] = text.split("\n").map(Number);
  return input.reduce(
    ({ counter, prev }, next) => {
      if (next > prev) {
        counter++;
      }
      return { counter, prev: next };
    },
    { counter: 0, prev }
  ).counter;
}

const part_1_one_line = (text) =>
  text
    .split("\n")
    .map(Number)
    .reduce(
      ({ counter, prev }, next) => ({
        prev: next,
        counter: prev === undefined ? 0 : next > prev ? counter + 1 : counter,
        // Note passing an empty object.
        // If we don't JS skips over the first iteration.
      }),
      {}
    ).counter;

function part_2(text) {
  let [a, b, c, ...input] = text.split("\n").map(Number);
  return input.reduce(
    ({ counter, a, b, c }, next) => {
      if (b + c + next > a + b + c) {
        counter++;
      }
      return { counter, a: b, b: c, c: next };
    },
    { counter: 0, a, b, c }
  ).counter;
}

// if name == "main" nodejs ES6 equivalent
// eslint-disable-next-line no-unused-vars
if (import.meta.url === `file://${process.argv[1]}`) {
  const text_input = uses_input();
  console.log("-- Part 1 --");
  console.log(part_1(text_input));
  console.log("(one line)");
  console.log(part_1_one_line(text_input));
  console.log("-- Part 2 --");
  console.log(part_2(text_input));
}
