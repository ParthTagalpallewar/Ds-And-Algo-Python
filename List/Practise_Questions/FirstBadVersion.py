def firstBadVersion(n, num):
        
        if n == 1:
            return 1
       
        start = 1
        end = n-1
        
        while start <= end:
            
            mid = (start + end) // 2
            
            if mid == num:
                end = mid - 1
                
            else:
                start = mid + 1
            
        return start 
if __name__ == '__main__':
    n = 5
    num = 4

    first = firstBadVersion(n, num)
    print('First Bad Version ', first)



    
            