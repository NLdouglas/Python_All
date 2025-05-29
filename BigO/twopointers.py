def twSum_ordenado(nums, target):
    left = 0
    right = len(nums) -1


    while left < right:
        soma = nums[left] + nums[right]

        if soma == target:
            return [left, right] # ou pode ser usado os valorres nums[left] e nums[right]
        
        elif soma < target:
            right += 1 # precisa de uma soma maior.
        else:
            right -= 1 # precisa de uma soma meenor
    
    return None # não achou nenhum par 