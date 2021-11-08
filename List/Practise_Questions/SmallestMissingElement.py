def missingNumber(arr,n):
        
        arr.sort()
        
        max = 1
        
        for i in arr:
            if i == max:
                max += 1
            elif i > max:
                return max
        return max
            
if __name__ == '__main__':
    
    list = [0, 1, 2, 3, 4, 5]
    n = len(list)

    missingNum = missingNumber(list, n)
    print("Missing Number is ", missingNum)
    