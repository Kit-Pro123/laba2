import random

def find_crat(x):
    while True:
        x_str = input(f"Введите цифру X: ")
        if x_str.isdigit() and len(x_str) == 1 and x_str!='0':
            x = int(x_str)
            break
        else:
            print("Некорректный ввод. Введите целое число.")
    nums = [random.randint(0, 200) for _ in range(10)]
    crat = list(filter(lambda number: number % x == 0, nums))
    print(f"Список чисел: {nums}")
    print(f"Числа, кратные {x}: {crat}")

find_crat(0)