def first_duplicate(nums: list) -> int:
    seen = set()
    
    for n in nums:
        if n in seen:
            return n
        else:
            seen.add(n)
    return -1     



print(first_duplicate([4, 3, 2, 7, 3, 1]))   # 3
print(first_duplicate([1, 2, 3, 4]))          # -1
print(first_duplicate([1, 1, 2, 3]))          # 1