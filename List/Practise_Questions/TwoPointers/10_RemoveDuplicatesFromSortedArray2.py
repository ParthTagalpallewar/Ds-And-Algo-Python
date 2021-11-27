def removeDuplicates(arr):
        
        n = len(arr)
        curr_ele = 0
        curr_count = 0
        
        left = 0
        right = 0
        
        for _ in range(n//2):
            
            while arr[left] == arr[right] and curr_count < 2:
                right += 1
                curr_count += 1
            
            curr_ele = arr[left]
            curr_count = 0

            left = right

            while arr[right] == curr_ele:
                right += 1
            
            arr[left] = arr[right]

            left += 1
            right = left

if __name__ == '__main__':
    
    list = [1,1,1,2,2,3]
    removeDuplicates(list)

    print(list)

    