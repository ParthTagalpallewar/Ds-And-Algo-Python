def SubArrayWithGivenSum(arr, n, sum):

    i = start = curr_sum = 0

    # Transverse in array
    while i < n and start < n:

        # if we find element
        if curr_sum == sum:
            return start, i-1

        # if curr_sum is less than required sum
        elif curr_sum < sum:
            curr_sum += arr[i]
            i += 1
        
        else:
            curr_sum -= arr[start]
            start += 1
    
    while start < n:
        if curr_sum == sum:
            return start, i-1
        else:
            sum -= arr[start]
            start += 1
    
    return -1

if __name__ == '__main__':
    
    list = [1,2,3,7,5]
    sum = 12

    e1, e2 = SubArrayWithGivenSum(list, len(list), sum)
    
    print(e1, " ", e2)
    
    sum = 0
    for i in range(e1, e2+1):
        sum += list[i]

    print("sum is ", sum)