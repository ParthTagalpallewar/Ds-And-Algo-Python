def nextLargerElement(arr,n):
        
    stack = []
    count = -1
    
    for i in range(n-1, -1, -1):

        num = arr[i]
        
        if count == -1:
            arr[i] = -1
            stack.append(num)
            count += 1
        else:
            while count > -1 and num >= stack[count]:
                stack.pop()
                count -= 1
        
            if count != -1:
                arr[i] = stack[count]
            else:
                arr[i] = -1

            stack.append(num)
            count += 1

    return arr
if __name__ == '__main__':
    
    arr = [6, 8, 0, 1, 3]
    nextLargestElement = nextLargerElement(arr, len(arr))
    print(nextLargestElement)
            