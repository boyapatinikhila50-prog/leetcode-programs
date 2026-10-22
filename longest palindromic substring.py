class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        start, end = 0, 0

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return length of the valid palindrome
            return right - left - 1

        for i in range(len(s)):
            # Odd length palindromes (e.g., "aba")
            len1 = expand_around_center(i, i)
            # Even length palindromes (e.g., "abba")
            len2 = expand_around_center(i, i + 1)
            
            max_len = max(len1, len2)
            
            if max_len > end - start:
                # Update starting and ending indices for the longest palindrome found
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]
