class Solution:
    def myAtoi(self, s: str) -> int:
        
        s_len = len(s)
        if s_len == 0:
            return 0
        
        nums = {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1}
        
        # move until the element is space
        startNum = 0
        while startNum < s_len and s[startNum] == ' ':
            startNum += 1
        
        # Now there must be possibility that number should be numeric, '+', '-', or alphabetic
        # lets check for '+', '-'
        multiplier = 1
        if startNum < s_len and s[startNum] == '-':
            multiplier = -1
            startNum += 1
        elif startNum < s_len and s[startNum] == '+':
            multiplier = 1
            startNum += 1
            
        # check for numeric
        if startNum < s_len and nums.get(s[startNum]) == 1:
            result = 0

            while startNum < s_len:
                # num is numeric
                if nums.get(s[startNum]) == 1:
                    result = (result * 10) + int(s[startNum])
                else:
                    break
                startNum += 1
            
            
            if (result * multiplier) < -2147483648:
                return -2147483648
            elif (result * multiplier) >= 2147483648:
                return 2147483647
            else:
                return result * multiplier
            
        # element will only alphabetic alphabetic
        else:
            return 0
        