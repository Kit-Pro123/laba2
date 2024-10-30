def get_number():
    for i in range(30):
        if i % 2 != 0:
            yield i

generator = get_number()
t = 0

for num in generator:
    if t == 0:
        print(f"Первое значение: {num}")
    if t == 4:
        print(f"Пятое значение: {num}")
    t += 1
    
print(f"Последнее значение: {num}")