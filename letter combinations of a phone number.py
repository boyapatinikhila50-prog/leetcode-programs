class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Mapping of digits to letters based on telephone keypad
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        res = []

        def backtrack(index, path):
            # If the current combination length equals digits length, add to results
            if index == len(digits):
                res.append(''.join(path))
                return

            # Explore all possible letters for the current digit
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()  # Backtrack

        backtrack(0, [])
        return res
