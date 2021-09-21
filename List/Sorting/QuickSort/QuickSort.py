

def findPivot(list, start, end):
    print("Def Find Pivot start :- ",start ," End  ", end )
    pi_index = start # index of pivot
    pi = list[pi_index] # pivot element-

    while start <= end:
       
        while start <= end and list[start] <= pi : 
            start+=1
            

        while list[end] > pi: 
            end -= 1
            

        if end > start:
            list[start], list[end] = list[end], list[start] # swap the bigger element we found with smaller element we found

    
        
    
    list[pi_index], list[end] = list[end], list[pi_index]
    print("List After Swapping ", list, "List [ ",end,"] = ", list[end] )
    print()

    return end

  


def quickSort(list, start, end):
    if start < end:
        print("def Quick Sort :- Start - ", start, " End - ", end)
        pi = findPivot(list, start, end)
        
        quickSort(list, start, pi-1)
        quickSort(list, pi+1, end)
        
        

# list = [11, 2, 4, 67, 768, 435, 3, 5]

print("List Before Reverse ", list, " Length ", len(list))
quickSort(list, 0, len(list)-1)
print(list)
