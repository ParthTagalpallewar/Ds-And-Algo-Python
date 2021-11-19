def countTriplet(arr, n):
    
    m = dict()
    res = 0

    for i in range(n):
        m[arr[i]] = 1

    for i in range(n-1):
        for j in range(i+1, n):
            
            val = abs(arr[i] + arr[j])
            if m.get(val) != None:
                res += 1
    return res
        


if __name__ == '__main__':
    
    list = [1, 2, 3, 5]
    count = countTriplet(list, len(list))	

    print("triplet count is ", count)    