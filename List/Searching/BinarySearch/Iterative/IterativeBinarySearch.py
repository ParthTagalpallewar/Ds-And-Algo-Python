
list = [10, 12, 14, 17, 25, 45, 46, 48, 53, 93, 111, 234]

n = 23

def interativeSearch(list, n):
    start = 0
    end = len(list) 

    for i in range(start, end):

        mid = (start + end)// 2

        if(list[mid] == n):
            return mid
        elif(list[mid] > n):
            end = mid - 1
        elif(list[mid] < n):
            start = mid + 1

    else:
        return -1

binaryIndex = interativeSearch(list, n)

print("Not Found") if(binaryIndex == -1) else print(binaryIndex)