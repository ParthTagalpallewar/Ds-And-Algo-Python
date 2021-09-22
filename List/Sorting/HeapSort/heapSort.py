def heapify(list, size, i):
    largest = i
    left = (2 * i) + 1
    right = (2 * i) + 2

    if(left < size and list[left] > list[largest]):
        largest = left

    if(right < size and list[right] > list[largest]):
        largest = right

    if(i != largest):
        #swap i with largest
        list[i], list[largest] = list[largest], list[i] 
        heapify(list, size, largest)

def heapSort(list): 
    n = len(list)

    #Building Max tree
    for i in range(n//2, -1, -1):
        heapify(list, n, i)

    for i in range(n-1, 0, -1):

        list[i], list[0] = list[0], list[i]

        heapify(list, i, 0)

arr = [1, 12, 9, 5, 6, 10]
heapSort(arr)
print(arr)