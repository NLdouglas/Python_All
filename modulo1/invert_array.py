def invert_array(nums):
    left = 0
    right = len(nums) -1
    
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        
        left += 1 
        right -= 1
    return nums


print(invert_array([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
print(invert_array([1, 2]))            # [2, 1]
print(invert_array([42]))              # [42]