def maxSubArraySum(arr,N):
    sum = 0
    best = -100000
    
    for i in range(N):
        sum += arr[i]
        
        best = max(best, sum)
        
        if sum < 0:
            sum = 0
            
            
    return best

if __name__ == '__main__':
    
    array = [-1, -1, 2]
    N = len(array)
    
    maxSum = maxSubArraySum(array, N)
    print("Max Sum is ", maxSum)
    