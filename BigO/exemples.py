#tempo constante (não aumenta com o tamanho da entrada)


def f_return(n):
    return n[0]
print(f_return(['teste', 'teste2', 'teste3']))  # O(1)


def calc_square(x, y):
    return x * y
print(calc_square(4, 5), "m²")  # O(1)


def calc_age(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(calc_age(10))  # O(1)

def string_length(string):
    if len(string) == 0:
        return True
    else:
        return False
print(string_length("3"))  # O(1)




# tempo linear ( aumenta com o tamanho da entrada) O(n)

nums = [ 1, 2,3 ]
sum(nums)       # sum of array
for n in nums:  #looping
    print(n)   

nums.insert(1, 100) #inserting an element
nums.remove(100)  # remove element
print(100 in nums)  # serch




# tempo quadrático (aumenta com o tamanho da entrada ao quadrado) O(n²)

nums_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(nums_2)):
    for j in range(len(nums_2[i])):
        print(nums_2[i]) 

# get every pair of elements in array 

nums_3 = [1, 2, 3, 4]
for i in range(len(nums_3)):
    for j in range(len(i + 1)):
        print(nums_3[i], nums_3[j]) 


# tempo logarítmico (aumenta com o tamanho da entrada logaritmicamente) O(log n)

#binary search O(log n)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6

l, r = 0, len(nums) - 1
while l <= r:
    mid = l + r // 2
    if target < nums[mid]:
        r = mid - 1
    elif target > nums[mid]:
        l = mid + 1
    else:
        print(mid)
        break

# binary search in a tree  O(log n)
def search(root, target):
    if not root:
        return False
    if target < root.val:
        return search(root.left, target)
    elif target > root.val:
        return search(root.right, target)
    else:
        return True