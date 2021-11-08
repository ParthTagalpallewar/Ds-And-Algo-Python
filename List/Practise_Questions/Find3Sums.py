def find3Sum(self, arr, n, sum):

    arr.sort()

    for i in range(n-2):

        left = i + 1
        right = n - 1

        while left < right:

            curr_sum = arr[i] + arr[left] + arr[right]

            if curr_sum == sum:
                return True
            
            elif curr_sum < sum:
                left += 1

            else:
                right -= 1
        
    return False

if __name__ == '__main__':
    # Driver program to test above function
    A = [1, 4, 45, 6, 0, 8]
    sum = 22
    arr_size = len(A)
    
    exists = find3Sum(None, A, arr_size, sum)

    print("Array Sum Exists ", exists)

    