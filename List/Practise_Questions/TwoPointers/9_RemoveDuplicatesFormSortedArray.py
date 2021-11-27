def RemoveDuplicates(nums, n):
    
        if len(nums) !=0:    
            current=nums[0]
            for i in nums[1:]:
                if current==i:
                    nums.remove(i)
                else:
                    current=i
        return len(nums)

        



if __name__ == '__main__':
    
    arr = [7, 7, 9, 9]
    n = len(arr)

    newArr = RemoveDuplicates(arr, n)
    print(newArr)