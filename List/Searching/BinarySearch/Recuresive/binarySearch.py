def binarySearch(list, n, start, end):

    if(start != end):
        mid = (start + end ) //  2
        midelement = list[mid]

        print("\nstart :- ", start, " end :- ", end , "  Mid :- ", mid, " MidElement  :-  ", midelement, "ListLength :- ",len(list) )
        

        if(n == midelement):
            print("midelement is found ", midelement, " \n")
            return mid # return index of given element
        elif(midelement > n):
            print("midelement is greater ", midelement, " \n")
            end = mid - 1
            return binarySearch(list = list, n = n,start =  start,end =  end)
        else:
            print("midelement is smaller ", midelement, " \n")      
            start = mid + 1
            return binarySearch(list = list, n = n,start =  start,end =  end)
    else:
        return -1
   
list = []

for i in range(0, 3000, 2):
    list.append(i)

n = 1972

index = binarySearch(list = list, n = n,start =  0,end =  len(list))

if(index != -1):
    print("Your Number index is ", index)
else:
    print("Not found")


""""

In Recursive :- 

time complexity  is n = log (n)
space Complexity n = log (n)

"""