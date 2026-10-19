#retorne o maior e menor sem usar min ou max 

def min_max(nums):
    num_max = nums[0] # start with the initial posistion from the array
    num_min = nums[0] 
    for i in nums: # passing a loop for to validade the value of each element (i) in the array nums
        if i > num_max:
            num_max = i 
        if i < num_min: 
            num_min = i
    return num_max, num_min

print(min_max([3, 7, 1, 9, 4]))  
print(min_max([5]))               
print(min_max([-3, -7, -1]))      