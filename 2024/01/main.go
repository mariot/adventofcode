package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	dat, err := os.ReadFile("input.txt")
	check(err)

	scanner := bufio.NewScanner(strings.NewReader(string(dat)))
	var columns [][]int

	for scanner.Scan() {
		line := scanner.Text()
		tokens := strings.Split(line, "   ")
		for i, token := range tokens {
			num, err := strconv.Atoi(token)
			check(err)
			if len(columns) <= i {
				columns = append(columns, []int{})
			}
			columns[i] = append(columns[i], num)
		}
	}

	for i := range columns {
		sort.Ints(columns[i])
	}

	sumOfDifferences := 0

	for i := 0; i < len(columns[0]); i++ {
		sumOfDifferences += int(math.Abs(float64(columns[0][i] - columns[1][i])))
	}
	fmt.Println(sumOfDifferences)

	counts := make(map[int]int)
	for _, num := range columns[1] {
		counts[num]++
	}

	sumOfAppearances := 0

	for _, num := range columns[0] {
		sumOfAppearances += num * counts[num]
	}
	fmt.Println(sumOfAppearances)
}
