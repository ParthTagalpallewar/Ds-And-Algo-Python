def insertationSort(list):

    for i in range(1, len(list)):
        j = i-1
        
        
        while(j >= 0 and list[j] > list[i]):
            
            list[i], list[j] = list[j], list[i]
          
            j -= 1
            i -= 1
          

    return list

list = [5, 4, 3, 2, 1]
print(insertationSort(list))