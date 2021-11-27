import sys
def closestPairToX(arr, X):
    n = len(arr)
    left = 0
    right = n-1

    maxDiff = sys.maxsize
    curr_diff = 0

    left_ele = right_ele = 0

    while left < right:
        
        curr_diff = abs((arr[left] + arr[right]) - X)

        if curr_diff < maxDiff:
            maxDiff = curr_diff
            left_ele = arr[left]
            right_ele = arr[right]
        
        if arr[left] + arr[right] < X:
            left += 1
        
        else:
            right -= 1

    return left_ele, right_ele

if __name__ == '__main__':
    arr = [10, 22, 28, 29, 30, 40]
    x = 54
    
    left, right = closestPairToX(arr, x)
    print("Closest pair is ", left,  " ", right)