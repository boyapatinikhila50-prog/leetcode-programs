class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # Pop the top element if stack is non-empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the popped bracket doesn't match the required open bracket
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto stack
                stack.append(char)

        # If stack is empty, all brackets were validly matched
        return not stack
