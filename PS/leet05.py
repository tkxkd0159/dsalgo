def expandAroundCenter(s, l, r):
    L = l
    R = r
    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1
    return R - L - 1

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s) < 1:
            return ""
        start = 0
        end = 0

        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i+1)
            final_len = max(len1, len2)
            if (final_len > end - start):
                start = i - (final_len - 1) // 2
                end = i + final_len // 2
        return s[start:end+1]
