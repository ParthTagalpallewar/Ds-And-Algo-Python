class Solution:
    	def countTriplet(self, arr, n):
	    
            triplets_count = 0
            
            arr.sort()
            
            for i in range(n):
                
                left = 0
                right = n-1
                
                while left < right:
                    
                    if left == i:
                        left += 1
                        continue
                    
                    elif arr[left] + arr[right] == arr[i]:
                        triplets_count += 1
                        left += 1
                        right -= 1
                    
                    elif arr[left] + arr[right] > arr[i]:
                        right -= 1
                    
                    else:
                        left += 1
            
            return triplets_count