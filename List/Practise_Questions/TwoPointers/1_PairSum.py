def isPairSum(arr, n, X):

    left = 0
    right = n-1

    while left < right:

        if arr[left] + arr[right] == X:
            return arr[left], arr[right]

        elif arr[left] + arr[right] > X:
            right -= 1

        else:
            left += 1

    return 0, 0 

if __name__ == '__main__':
    arr = [3, 5, 9, 2, 8, 10, 11]
    val = 17
    
    left, right = isPairSum(arr, len(arr), val)
    print(left, " ", right)