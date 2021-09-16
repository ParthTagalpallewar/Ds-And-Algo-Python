def mergeSort(arr):
    if(len(arr) > 1):

        lArr = arr[:len(arr)//2] # left half array
        rArr = arr[len(arr)//2:] # right half array

        newArr = mergeSort(lArr)
        newArr2 = mergeSort(rArr)
       
        return mergeArray(newArr, newArr2)
    else:
        return arr

def mergeArray(lArr, rArr):
  
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
    
    
    return sortedArr

list = [5, 4, 3, 2, 1]
list = mergeSort(list)

print(list)