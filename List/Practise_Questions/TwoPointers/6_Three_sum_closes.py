import sys
def threeSumClosest(arr, target: int):
    n = len(arr)
    arr.sort()
    closest = sys.maxsize
    curr_close = 0
    max_sum = 0
    
    for i in range(n):
        
        left = 0
        right = n-1
        
        while left < right:
            
            if left == i:
                left+= 1
                continue
        
            if right == i:
                right -= 1
                continue
            
            if i in [3, 7 , 8] and left in [3, 7, 8] and right in [3, 7, 8]:
                print(i, left, right)
            
            curr_close = abs(target - (arr[i] + arr[left] + arr[right]))

            if curr_close < closest:
                closest = curr_close
                max_sum = (arr[i] + arr[left] + arr[right])
            
            if arr[left] + arr[right] > target:
                right -= 1
            
            else:
                left += 1
        
           
    
    return max_sum  

if __name__ == '__main__':
    list = [-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]
    target = 0

    closest = threeSumClosest(list, target)
    print("Closest Num is ", closest)
    