WATER_PER_KG = 30
ML_IN_LITER = 1000


print("Добро пожаловать это FitLifebot")
user_name = input("Как вас зовут? ").title()

while True:
    try:
        user_age = int(input("Сколько вам лет? "))
        break
    except ValueError:
        print("Ошибка! Пожалуйста введите только цифры.")

while True:
    try:
        user_weight = float(input("Какой у вас вес? (кг): "))
        break
    except ValueError:
        print("Ошибка! Пожалуйста введите только цифры")

while True:
    try:
        user_height = float(input("Какой у вас рост? (м): "))
        if user_height <= 0:
            print("Ошибка! Рост должен быть положительным")
        break
    except ValueError:
        print("Ошибка! Пожалуйста введите только цифры")

bmi = round(user_weight / (user_height ** 2), 1)
water_l = user_weight * WATER_PER_KG / ML_IN_LITER

print("Отчет для пользователя:")
print(f"Имя: {user_name}\n"
      f"Возраст: {user_age}лет\n"
      f"Ваш индекс массы тела: {bmi}\n"
      f"Рекомендуемая норма воды: {water_l:.1f}л. в день")
print("Расчет окончен. Будьте здоровы!")
