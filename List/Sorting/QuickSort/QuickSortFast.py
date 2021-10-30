
# 11, 2, 4, 67, 768, 435, 3, 5
def findPivot(arr, low, high):

    pivot = arr[high]
    piIndex = low

    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[piIndex] = arr[piIndex], arr[i]
            piIndex += 1
        
    arr[piIndex], arr[high] = arr[high], arr[piIndex]
    return piIndex 

    


def quickSort(list, start, end):
    if start < end:
        print("def Quick Sort :- Start - ", start, " End - ", end)
        pi = findPivot(list, start, end)
        
        quickSort(list, start, pi-1)
        quickSort(list, pi+1, end)
        
        

list = [11, 2, 4, 67, 768, 435, 3, 5]

print("List Before Reverse ", list, " Length ", len(list))
quickSort(list, 0, len(list)-1)
print(list)
