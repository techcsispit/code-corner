package main

import (
	"fmt"
	"strings"
)

var numerals = []struct {
	value  int
	symbol string
}{
	{1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"}, {90, "XC"},
	{50, "L"}, {40, "XL"}, {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"},
}

func main() {
	var n int
	fmt.Scan(&n)
	var out strings.Builder
	for _, r := range numerals {
		for n >= r.value {
			out.WriteString(r.symbol)
			n -= r.value
		}
	}
	fmt.Println(out.String())
}
