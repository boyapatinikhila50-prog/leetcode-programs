class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Take the first string as reference
        prefix = strs[0]

        for i in range(len(prefix)):
            char = prefix[i]
            # Check character against the same position in other strings
            for s in strs[1:]:
                # If index exceeds length or character doesn't match
                if i == len(s) or s[i] != char:
                    return prefix[:i]

        return prefix
