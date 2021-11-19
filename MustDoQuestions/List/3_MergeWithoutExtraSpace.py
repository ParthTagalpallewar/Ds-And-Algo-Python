def merge(arr1,arr2,n,m):
    
    j = 0
    i = n-1
   
    while i > -1 and j < m:
       
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            j += 1
        i -= 1

    a = sorted(arr1)
    b = sorted(arr2)

    for i in range(n):
        arr1[i] = a[i]

    for i in range(m):
        arr2[i] = b[i]

if __name__ == '__main__':
    list1 = [1, 3, 5, 7] 
    list2 = [0, 2, 6, 8, 9]

    merge(list1, list2, len(list1), len(list2))
    
    print(list1+list2)