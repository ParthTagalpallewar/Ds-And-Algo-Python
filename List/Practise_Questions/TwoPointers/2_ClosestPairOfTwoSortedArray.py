import sys
def closestPair(arr1, arr2, m, n, X):
    left = 0 
    right = n-1

    maxDiff = sys.maxsize
    curr_diff = 0

    arr1_ele = 0
    arr2_ele = 0


    while left < n and right >= 0:

        curr_diff = abs((arr1[left] + arr2[right]) - X)

        if curr_diff < maxDiff:
            maxDiff = curr_diff
            arr1_ele = arr1[left]
            arr2_ele = arr2[right]

        elif arr1[left] + arr2[right] > X:
            right -= 1
        
        else:
            left += 1
    
    return arr1_ele, arr2_ele

if __name__ == '__main__':
    
    arr1 = [1, 4, 5, 7]
    arr2 = [10, 20 , 30, 40]
    X = 50


    left, right = closestPair(arr1, arr2, len(arr1), len(arr2), X) 
    print("Closest Pair is ", left, " ", right )