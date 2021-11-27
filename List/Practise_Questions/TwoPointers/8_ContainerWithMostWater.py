def maxArea(arr, n):

    left = 0
    right = n-1

    max_area = curr_area = 0

    while left < right:

        curr_area = min(arr[left], arr[right]) * (right - left)

        if arr[left] < arr[right]:
            left += 1

        else:
            right -= 1

        max_area = max(max_area, curr_area)

    return max_area


if __name__ == '__main__':
    
    list = [1,2,3,100,100, 3, 2, 1]
    max_area = maxArea(list, len(list))
    print('Max Area Needed is ', max_area ) 
    

