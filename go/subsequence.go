package main

import "fmt"

func isSubsequence(s string, t string) bool {
	p := 0

	for i := 0; i < len(t); i++ {
		if s[p] == t[i] {
			p++
		}
	}

	fmt.Println(p)
	fmt.Println(len(s))
	if p == len(s) {
		return true
	}

	return false
}

func main() {
	var s string = "abc"
	var t string = "axsdbsdc"

	isSubsequence(s, t)
}
