package main

import (
	"bufio"
	"fmt"
	"os"
	"path"
	"runtime"
	"strconv"
	"strings"
)

type Command struct {
	direction string
	val       int
}

const testInput = `forward 5
down 5
forward 8
up 3
down 8
forward 2`

// No builtin absolute value for integers
// Don't ask me why. So here's a quick one.
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func readInput() []*Command {

	_, filename, _, _ := runtime.Caller(0)
	file, _ := os.Open(path.Dir(filename) + "/input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var input []*Command
	for scanner.Scan() {
		line := strings.Fields(scanner.Text())
		val, _ := strconv.Atoi(line[1])
		command := Command{direction: line[0], val: val}
		input = append(input, &command)
	}
	return input
}

func part1() int {
	horizontal, vertical := 0, 0
	for _, command := range readInput() {
		switch command.direction {
		case "forward":
			horizontal += command.val
		case "up":
			vertical += command.val
		case "down":
			vertical -= command.val
		}
	}
	return abs(horizontal * vertical)
}

func part2() int {
	depth, aim, horizontal := 0, 0, 0
	for _, command := range readInput() {
		switch command.direction {
		case "forward":
			horizontal += command.val
			depth += aim * command.val
		case "up":
			aim += command.val
		case "down":
			aim -= command.val
		}
	}
	return abs(horizontal * depth)
}

func main() {
	fmt.Println("-- Part 1 --")
	fmt.Println(part1())
	fmt.Println("-- Part 2 --")
	fmt.Println(part2())
}
