
# Calculate Minimum steps needed to reach to end of array


def minimumJumps(nums, n):
  
    previous = 0
    current = 0 
    jumps = 0
    
    for i in range(n):
        if(i > previous):
            jumps += 1
            previous = current  
        
        current = max(current, i + nums[i])
    
    return jumps

if __name__ == '__main__':
    
    list = [1, 2, 3, 5, 6, 7, 1, 1, 1]
    N = len(list)

    minJumps = minimumJumps(list, N)
    print("Mimimum Jumps Required Are ", minJumps)

    