
"""
Time Complexity For Linear Search 

Best Case : O(1) 
Worst Case : O(n)

"""


def linearSearch(list, n):

    for i in range(0, len(list)):
        if(list[i] == n):
            return i
    else:
        return -1

list = [100, 300, 800]
numberToSearch = 30

#Returning Index of Number In List
indexOfNumber = linearSearch(list, numberToSearch)

print("index is ", indexOfNumber) if(indexOfNumber != -1) else print("Number Not found")
