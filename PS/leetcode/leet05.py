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

    # DP, slower than first method
    def longestPalindrome2(self, s: str) -> str:    
        n = len(s)
        res = ""
        if n < 1 or s is None:
            return ""
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n, 1):
                matrix[i][j] = (s[i] == s[j]) and (j - i < 3 or matrix[i+1][j-1])
                
                if matrix[i][j] and (j+1-i) > len(res):
                    res = s[i:j+1]
              
        return res
