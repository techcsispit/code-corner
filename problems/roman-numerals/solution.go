package main

import (
	"fmt"
	"strings"
)

var numerals = []struct {
	value  int
	symbol string
}{
	{1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
	{100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"},
	{10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"},
}

func main() {
	var inputNum int
	fmt.Scan(&inputNum)
	var out strings.Builder
	for _, romanEntry := range numerals {
		for inputNum >= romanEntry.value {
			out.WriteString(romanEntry.symbol)
			inputNum -= romanEntry.value
		}
	}
	fmt.Println(out.String())
}
