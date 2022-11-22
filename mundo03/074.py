from random import randint
nums = []
for i in range(5):
    nums.append(randint(0,1000))
nums = tuple(nums)
print(f'A tupla formada foi: {nums}')
print(f'O maior valor é {max(nums)}')
print(f'O menor valor é {min(nums)}')


"""  

ou:
from random import randint
nums = []
for i in range(5):
    nums.append(randint(0,1000))
nums = tuple(nums)
print(f'A tupla formada foi: ', end='')
for i in range(5):
    print(nums[i], end=' ')
print(f'\nO maior valor é {max(nums)}')
print(f'O menor valor é {min(nums)}')

"""