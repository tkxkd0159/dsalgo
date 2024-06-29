package algo_test

import (
	"algo"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestIsPalindrome(t *testing.T) {
	require.True(t, algo.IsPalindrome("radar"))
	require.True(t, algo.IsPalindrome("madam"))
	require.True(t, algo.IsPalindrome("kayak"))
	require.True(t, algo.IsPalindrome("racecar"))
	require.True(t, algo.IsPalindrome("tattarrattat"))
}
