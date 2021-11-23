def maxArea(heights):
        
        N = len(heights)
        
        left = 0
        right = N-1
        
        curr_area = 0
        max_area = 0
        
        
        while left < right:
            
            curr_area = min(heights[left], heights[right]) * abs(right-left)
            
            if heights[left] < heights[left+1] and left+1 != right:
                left += 1
            elif heights[right] < heights[right-1] and right-1 != left:
                right -= 1 
            else:
               break
        
            max_area = max(curr_area, max_area)
            
        while left < N and right < N:
            
            curr_area = min(heights[left], heights[right]) * abs(right-left)
            
            left += 1
            right += 1
        
            max_area = max(curr_area, max_area)
    
        return max(curr_area, max_area)

if __name__ == '__main__':
    
    list = [1,3,2,5,25,24,5]
    max_area = maxArea(list)
    print('Max Area Needed is ', max_area ) 
    
