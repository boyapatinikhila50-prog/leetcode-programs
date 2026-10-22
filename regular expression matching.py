class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # Base case: if pattern is fully consumed, string must also be fully consumed
            if j == len(p):
                return i == len(s)

            # Check if current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # If the next character in pattern is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Two cases:
                # 1. Skip the '*' and its preceding element (match 0 times)
                # 2. Use the '*' if there's a match, advancing index i in s
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Regular match, move both pointers forward
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
