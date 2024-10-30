import datetime

def find_age():
    while True:
        birthdate_str = input("Введите дату рождения в формате ДД/ММ/ГГГГ: ")
        parts = birthdate_str.split('/')
        if len(parts) != 3:
            print("Некорректный формат даты. Введите дату в формате ДД/ММ/ГГГГ.")
            continue
        for part in parts:
            if not part.isdigit():
                print("Дата рождения должна состоять только из цифр.")
                continue
        day, month, year = map(int, parts)
        if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= datetime.date.today().year):
            print("Некорректная дата рождения.")
            continue
        break
    birthdate = datetime.date(year, month, day)
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    print(f"Ваш возраст: {age} лет")

find_age()