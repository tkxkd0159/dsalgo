//package main
//
//import (
//	"ljs/baekjoon/base/io"
//)
//
//func main() {
//	io.Solve10926()
//}

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	Solve()
}

func Solve() {
	ans := [6]int{1, 1, 2, 2, 2, 8}
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	line := scanner.Text()
	numset := strings.Split(line, " ")
	for i, limit := range ans {
		target, _ := strconv.Atoi(numset[i])
		res := limit - target
		ans[i] = res
	}

	for _, elem := range ans {
		fmt.Printf("%d ", elem)
	}

}
