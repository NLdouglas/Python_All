nums = [2,7,11,15]
target = 9
for x in range(len(nums)):
    for y in range(x + 1, len(nums)):
        if nums[x] + nums[y] == 9:
            print(x, y)


numeros = set()
for x in nums:
    complemento = nums - target
    if complemento in numeros:
        print(numeros[complemento], x)
    numeros.add(x)

