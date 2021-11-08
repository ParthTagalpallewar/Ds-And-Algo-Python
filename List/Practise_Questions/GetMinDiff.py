def getMinDiff(array, n, k):
    
    arr = sorted(array)

    smallest, largest = arr[0]+k, arr[n-1]-k
    
    ans = arr[n-1] - arr[0]
    
    
    
    for i in range(n-1):
        mi = min(smallest, arr[i+1]-k)
        ma = max(largest, arr[i]+k)
        
        if mi < 0: continue
        
        ans = min(ans, ma-mi)
        
    return ans

if __name__ == '__main__':
    list = [1, 5, 8, 10]
    K = 4
    N = len(list)
    
    minDiff = getMinDiff(list, N, K)
    print("Minimum Difference is ", minDiff)