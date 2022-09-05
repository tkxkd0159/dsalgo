package base

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func Solve2753() {
	s := bufio.NewScanner(os.Stdin)
	s.Scan()
	year, _ := strconv.Atoi(s.Text())

	check := 0
	if (year%4 == 0) && (year%100 != 0) {
		check = 1
	} else if year%400 == 0 {
		check = 1
	}
	fmt.Printf("%d", check)
}

func Solve14681() {
	//var coord [2]int
	//ilen := 2
	//for i:=0;i<ilen;i++{
	//	fmt.Scanf("%d", &coord[i])
	//}

	ilen := 2
	coord := [2]int{}
	s := bufio.NewScanner(os.Stdin)
	for i := 0; i < ilen; i++ {
		s.Scan()
		coord[i], _ = strconv.Atoi(s.Text())
	}

	var ans int
	if coord[0] > 0 {
		if coord[1] > 0 {
			ans = 1
		} else {
			ans = 4
		}
	} else {
		if coord[1] > 0 {
			ans = 2
		} else {
			ans = 3
		}
	}
	fmt.Println(ans)
}

func Solve2884() {
	var h, m int
	fmt.Scanf("%d %d", &h, &m)
	m -= 45
	if m < 0 {
		m += 60
		if h--; h < 0 {
			h += 24
		}
	}
	fmt.Printf("%d %d", h, m)
}
