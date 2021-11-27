def fourSum(arr, target: int):
       
    n = len(arr)
    arr.sort()
    
    answer = []
    
    for i in range(n-1):
        for j in range(i+1, n):
            
            left = j + 1
            right = n - 1 
            
            while left < right:
                total = arr[i] + arr[j] + arr[left] + arr[right]
                
                if total < target:
                    left += 1
                
                elif total > target:
                    right -= 1
                
                else:
                    answer.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
    return answer
                    
if __name__ == '__main__':
    
    list = [2,2,2,2,2]
    target = 8

    data = fourSum(list, target) 
    print(data)