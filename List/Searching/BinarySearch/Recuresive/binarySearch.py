def binarySearch(list, n, start, end):

    if(start != end):
        mid = (start + end ) //  2
        midelement = list[mid]

        # print("\nstart :- ", start, " end :- ", end , "  Mid :- ", mid, " MidElement  :-  ", midelement, "ListLength :- ",len(list) )
        

        if(n == midelement):
            # print("midelement is found ", midelement, " \n")
            return mid # return index of given element
        elif(midelement > n):
            # print("midelement is greater ", midelement, " \n")
            end = mid - 1
            return binarySearch(list = list, n = n,start =  start,end =  end)
        else:
            # print("midelement is smaller ", midelement, " \n")      
            start = mid + 1
            return binarySearch(list = list, n = n,start =  start,end =  end)
    else:
        return -1
   
list = list(set(r for r in range(1000000)))

print(binarySearch(list = list, n = 20,start =  0,end =  len(list)))




""""

In Recursive :- 

time complexity  is n = log (n)
space Complexity n = log (n)

"""