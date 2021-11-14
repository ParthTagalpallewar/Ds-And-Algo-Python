def getMinDiff(array, n, k):
    
    arr = sorted(array)

    smallest, largest = arr[0]+k, arr[n-1]-k
    
    ans = arr[n-1] - arr[0]
    
    print(arr)

    print(arr[0], " ", arr[n-1])
    
    for i in range(n-1):

        a = arr[i+1]-k
        b = arr[i]+k

        mi = min(smallest, arr[i+1]-k)
        ma = max(largest, arr[i]+k)

        if mi < 0: continue

        print(arr[i+1], " ", arr[i], " ", mi, " ", ma)
        
        
        ans = min(ans, ma-mi)
        
    return ans

if __name__ == '__main__':
    list = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1]
    K = 5
    N = len(list)
    
    minDiff = getMinDiff(list, N, K)
    print("Minimum Difference is ", minDiff)