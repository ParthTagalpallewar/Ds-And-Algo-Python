
def getMinDiff(arr, n, K):
        
        g_idx = s_idx = 0
        
        for i in range(1, n):
            if arr[i] > arr[g_idx]:
                g_idx = i
                
            if arr[i] < arr[s_idx]:
                i_idx = i
        
        arr[g_idx] -= K
        arr[s_idx] += K
        
        return arr[g_idx] - arr[s_idx]

if __name__ == '__main__':
    
    K = 2
    list = [1, 5, 8, 10]
    n  = len(list)

    min_diff = getMinDiff(list, n, K)

    print(min_diff)
    