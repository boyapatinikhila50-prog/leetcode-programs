class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Determine the sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse digits
        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
            
        reversed_x *= sign
        
        # Check 32-bit signed integer boundaries
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
            
        return reversed_x
