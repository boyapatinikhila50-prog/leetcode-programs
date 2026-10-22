class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #Map values to Roman symbols in descending order (including subtractive combinations)
        val_to_roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
            (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
            (1, 'I')
        ]
        
        roman = []
        for val, symbol in val_to_roman:
            if num == 0:
                break
            count, num = divmod(num, val)
            roman.append(symbol * count)
            
        return ''.join(roman)
