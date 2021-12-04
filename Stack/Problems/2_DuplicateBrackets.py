def duplicateBrackets(s, n):

    stack = []
    count = -1

    
    for i in range(n):
        if s[i] != ')':
            stack.append(s[i])
            count += 1
        else:
            
            if stack[count] == '(':
                return True
            
            while stack[count] != '(':
                stack.pop()
                count -= 1
            
            stack.pop()
            count -= 1

    return False

if __name__ == '__main__':
    string = '((a+b))+(b+c)'
    isValid = not duplicateBrackets(string, len(string))
    print(isValid)    
          

            