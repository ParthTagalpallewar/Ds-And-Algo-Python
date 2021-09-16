def mergeSort(arr):
    print(" ")
    print("List ", arr)
    if(len(arr) > 1):
        lArr = arr[:len(arr)//2] # left half array
        rArr = arr[len(arr)//2:] # right half array
        print(lArr ,"   ", rArr)


        mergeSort(lArr)
        mergeSort(rArr)
       
        return mergeArray(lArr, rArr)
    else:
        return arr

def mergeArray(lArr, rArr):
  
    print("Got ", lArr , "  ", rArr, "  For merging")
    sortedArr = []
    
    li = ri = 0

    while(li < len(lArr) and ri < len(rArr)):

        #check left is small and append
        if(lArr[li] < rArr[li]):
            sortedArr.append(lArr[li])
            li += 1
        else:
            sortedArr.append(rArr[ri])
            ri += 1
    
    # if any element left in left array
    while(li < len(lArr)):

        sortedArr.append(lArr[li])
        li += 1
    
    # if any elements left in right array
    while(ri < len(rArr)):
        sortedArr.append(rArr[ri])
        ri += 1
    
    print("Returing Sorted Array ", sortedArr , end = "\n\n")
    return sortedArr

list = [5, 4, 3, 2, 1]
list = mergeSort(list)

print(list)