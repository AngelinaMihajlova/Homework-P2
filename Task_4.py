# Реализуйте выдачу случайного числа. Не использовать random.randint и вообще библиотеку random.
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - 
# для задания случайности. Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import time

def rand_val(x, y):
   sub = y - x
   random = int(time.time() * 1000) 
   random %= sub
   random += x
   return random

x = int(input('Enter x: '))
y = int(input('Enter y: '))
print(rand_val(x, y))