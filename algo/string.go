package algo

func IsPalindrome(word string) bool {
	for i := range len(word) / 2 {
		if word[i] != word[len(word)-1-i] {
			return false
		}
	}

	return true
}
