def search(list, start, end, n):

    if(start > 0 or end <= len(list)):

        
        chunk = (end-start)//3
        m1 = chunk + start
        m2 = start + chunk * 2

        # print("  M1 ", m1 )

        #Check m1 first
        if(n == list[m1]):
            print("found number ", list[m1])
            return m1
        #check m2
        elif(n == list[m2]):
            return m2
        #if given number is smaller than m1
        elif(n < list[m1]):
            return search(list, start, m1 - 1, n)
        # n in betwen m1 and m2
        elif(list[m1] < n < list[m2]):
            return search(list, m1 + 1, m2 - 1, n)
        # n is greater than m2
        elif(list[m2] < n):
            return search(list, m2 + 1, end, n)
    else :
        return -1


# print("starts")
list = list(set(r for r in range(1000000)))


print(search(list = list,start= 0,end= len(list),n= 20))
# print("ended")