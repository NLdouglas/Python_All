def count_pairs(nums: list, target: int) -> int:
    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)): 
            if nums[i] + nums[j] == target:
                count += 1
    
    return count
               
    
            


# Testes
print(count_pairs([1, 2, 3, 4, 5], 6))   # 2
print(count_pairs([1, 1, 1, 1], 2))       # 6
print(count_pairs([1, 2, 3], 10))         # 0