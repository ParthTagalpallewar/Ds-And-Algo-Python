def PositiveAndNegativeSeperator(arr, N):
    
    # left = 0
    # right = N-1
    
    # while left < N//2 and right > N//2:

    #     # move till we find positive element
    #     while left < N and arr[left] < 0:
    #         left += 1

    #     while right > 0 and arr[right] > 0:
    #         right -= 1

    #     arr[left], arr[right] = arr[right], arr[left]
    #     left += 1
    #     right -= 1

    # return arr 
    
    
    j = 0
    for i in range(N):
        if arr[i] < 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr

        



if __name__ == '__main__':
    list = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    n = len(list)

    seperated = PositiveAndNegativeSeperator(list, n)
    print("List ", seperated)