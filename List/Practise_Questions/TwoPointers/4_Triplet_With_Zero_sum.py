def findTriplets(arr, n):
        
    arr = sorted(arr)
        
    for i in range(n):
        
        left = i + 1
        right = n-1
        
        while left < right:
            
            if arr[i] + arr[left] + arr[right] == 0:
                print(arr[i], " ", arr[left], " ", arr[right])
                return 1
            elif arr[i] + arr[left] + arr[right] > 0:
                right -= 1
            else:
                left += 1
        
    return 0

if __name__ == '__main__':
    
    arr = [-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]
    
    print(findTriplets(arr, len(arr)))