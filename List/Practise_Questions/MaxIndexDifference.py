def maxIndexDiff(A, N): 
        m = i = 0
        j = N-1
        
        while i <= j:

            I_Element = A[i]
            J_Element = A[j]
            
            if A[i] <= A[j]:
                m = max(m, j-i)
                i += 1
                j = N-1
            else:
                j -= 1
        
        return m
if __name__ == '__main__':
    
   
   A = [34, 8, 10, 3, 2, 80, 30, 33, 1]
   N = len(A)

   maxIndex = maxIndexDiff(A, N) 
   print("Max Index is ", maxIndex)