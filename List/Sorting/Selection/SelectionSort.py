A = [64, 25, 12, 22, 11]
 
# Traverse through all array elements
for i in range(len(A)):
     
    minIndex = i

    for j in range(i+1, len(A)):
        if(A[minIndex] > A[j]):
            minIndex = j

    A[i], A[minIndex] = A[minIndex], A[i]

print(A)