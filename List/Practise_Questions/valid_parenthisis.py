def isValid(s: str):
        
        res = []
        
        for i in range(len(s)):
            reversed = getReversed(s[i])
            if s[i] in ['(', '[', '{']:
                res.append(s[i])
            elif len(res) == 0 or res[-1] == getReversed(s[i]):
                res.pop()
                continue
            else:
                return False
        
        return True if len(res) == 0 else False
        
        

def getReversed(s: str):
    if s == '(':
        return ')'
    elif s == ')':
        return '('
    
    if s == '{':
        return '}'
    elif s == '}':
        return '{'

    if s == '[':
        return ']'
    elif s == ']':
        return '['

    
    

if __name__ == '__main__':
    
    is_valid = isValid("()[")
    print(is_valid)
    