def count_frequency(nums: list) -> dict:
    freq = {}
    
    for n in nums:
        if n not in freq:
              freq[n] = 0 # cria uma chave com o valor 0 no dicionario caso N nao esteja em freq          
        freq[n] = freq[n] + 1

    freq_two = {}
    for n2 in nums:
         freq_two[n2] = freq_two.get(n2, 0) + 1

    return freq, freq_two

    
         

# Testes
print(count_frequency([1, 2, 2, 3, 3, 3]))   # {1: 1, 2: 2, 3: 3}
print(count_frequency([5, 5, 5, 5]))          # {5: 4}
print(count_frequency([1, 2, 3]))             # {1: 1, 2: 1, 3: 1}