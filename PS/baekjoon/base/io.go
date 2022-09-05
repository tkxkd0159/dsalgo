package base

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func Solve10926() {
	var a string
	fmt.Scanf("%s", &a)
	fmt.Printf("%s\n", a+"??!")
}

func Solve18108() {
	var a int
	fmt.Scanf("%d", &a)
	fmt.Printf("%d\n", a-543)
}

func Solve25083() {
	fmt.Println(`         ,r'"7`)
	fmt.Println("r`-_   ,'  ,/")
	fmt.Println(` \. ". L_r'`)
	fmt.Println("   `~\\/")
	fmt.Println("      |")
	fmt.Println("      |")
}

func Solve3003() {
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
