class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge case: single row or input length smaller than/equal to numRows
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of strings to store characters for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            
            # Reverse direction when reaching top or bottom boundary
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move up or down based on direction
            current_row += 1 if going_down else -1

        # Concatenate all rows to form the final result
        return ''.join(rows)
        
