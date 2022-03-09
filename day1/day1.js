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
    .reduce(({ counter, prev }, next) => ({
      prev: next,
      counter: prev === undefined ? 0 : next > prev ? counter + 1 : counter,
      // Note passing an empty object.
      // If we don't JS skips over the first iteration.
    }), {}).counter;

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

console.log("-- Part 1 --");
console.log(part_1(test_input));
console.log("(one line)");
console.log(part_1_one_line(test_input));
console.log("-- Part 2 --");
console.log(part_2(test_input));
