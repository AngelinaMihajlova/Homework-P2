# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial. Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = input("Введите число: ") 
while n.isalpha():
    print('Вы ввели не число')
    n = input("Введите число: ") 
n = int(n)

def find_factorial(n):
    f = 1
    fact = []
    for i in range(1, n + 1):
        f *= i
        fact.append(f)
    return fact

print(find_factorial(n))