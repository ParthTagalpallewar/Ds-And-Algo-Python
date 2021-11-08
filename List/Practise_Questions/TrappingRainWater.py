class Solution:
    def trappingWater(self, arr, n):
        
        #left biggest building array
        lMax = arr[0]
        left = []
        for i in range(n):
            lMax = max(lMax, arr[i])
            left.append(lMax)
         
        rMax = arr[n-1] 
        right = []
        for i in range(n-1, -1, -1):
            rMax = max(rMax, arr[i])
            right.append(rMax)
        
        #revese right list
        right = self.Reverse(right)
           
        water = 0
        
        for i in range(n):
            #smallest element form left and right array
            smallest = min(left[i], right[i])
            
            water += smallest - arr[i]
            
        return water

    def Reverse(self, lst):
        return [ele for ele in reversed(lst)]

if __name__ == '__main__':

    list = [3,0,0,2,0,4]    
    N = len(list)

    sol = Solution()
    waterStored = sol.trappingWater(list, N)
    print("Blocks of Water Can be Saved ", waterStored)