def removeDuplicates(nums1, nums2):
    
        m = len(nums1)
        n = len(nums2)
        
        median = 0
        
        if (m+n) % 2 == 0:
            median = (nums1[m-1] + nums2[0]) / 2
        else:
            median = min(nums1[m-1], nums2[0])
        
        return median


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]

    median = removeDuplicates(nums1, nums2)
    print(median)