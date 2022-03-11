package main

import (
	"bufio"
	"fmt"
	"os"
	"path"
	"runtime"
	"strconv"
)

const testInput = `199
200
208
210
200
207
240
269
260
263`

func readInput() []int {

	_, filename, _, _ := runtime.Caller(0)
	file, _ := os.Open(path.Dir(filename) + "/input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var input []int
	for scanner.Scan() {
		val, _ := strconv.Atoi(scanner.Text())
		input = append(input, val)
	}
	return input
}

func part1() int {
	counter := 0
	numbers := readInput()
	prev := numbers[0]
	for _, next := range numbers[1:] {
		if next > prev {
			counter++
		}
		prev = next
	}
	return counter
}

func part2() int {
	counter := 0
	numbers := readInput()
	a, b, c := numbers[0], numbers[1], numbers[2]
	for _, next := range numbers[3:] {
		if b+c+next > a+b+c {
			counter++
		}
		a, b, c = b, c, next
	}
	return counter
}

func main() {
    fmt.Println("-- Part 1 --")
	fmt.Println(part1())
    fmt.Println("-- Part 2 --")
	fmt.Println(part2())
}
