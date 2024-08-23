class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            if i < len(s) and (s[i] == p[j] or p[j] == '?') : 
                memo[(i, j)] =  dp(i + 1, j + 1)
            elif p[j] == '*':
                memo[(i, j)] = dp(i, j + 1) or (i < len(s) and dp(i + 1, j))
            else: 
                memo[(i, j)] = False
            return memo[(i, j)]
        return dp(0, 0)
