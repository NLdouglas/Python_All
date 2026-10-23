def two_sum_map(nums: list, target: int) -> int:
    seen = {}

    for i, n in enumerate(nums): # para cade chave(i) e valor (n) em lista (nums)
        complent = target - n
        if complent in seen:
            return [seen[complent], i] # retorna os dois index, complement passa a ser a chave(i) de seen, pegando o index de i(nums)
        else:
            seen[n] = i # adicionar a chave(i) no valor(n) de seen
    return []
    







# Testes
print(two_sum_map([2, 7, 11, 15], 9))    # [0, 1]
print(two_sum_map([3, 2, 4], 6))         # [1, 2]
print(two_sum_map([3, 3], 6))            # [0, 1]