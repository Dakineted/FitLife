# Проект FitLife - MVP версия 1.0


# 1. Знакомство
# TODO: Запрос имени, возраста пользователя.
print("-" * 40)
print(" 😊 Добро пожаловать это FitLifebot 😊")
print("-" * 40)
user_name = input("Как вас зовут? ")
user_name = user_name.title()
while True:
    user_input_age = input("Сколько вам лет? ")
    try:
        user_age = int(user_input_age)
        break
    except ValueError:
        print("Ошибка! Пожалуйста введите только цифры.")
# 2. Сбор данных
# TODO: Запрос веса и роста пользователя.
while True:
    user_input_weight = input("Какой у вас вес? (кг): ")
    try:
        user_weight = float(user_input_weight)
        break
    except ValueError:
        print("Ошибка! Пожалуйста введите только цифры")
while True:
    user_input_height = input("Какой у вас рост? (м): ")
    try:
        user_height = float(user_input_height)
        if user_height <= 0:
            print("Ошибка! Рост должен быть положительным")
        break
    except ValueError:
        print("Ошибка! Пожалуйста введите только цифры")
# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# TODO: Расчет индекса массы тела.
bmi = round(user_weight / (user_height ** 2), 1)
# TODO: Присвоение констант, расчет нормы воды, перевод в литры.
WATER_PER_KG = 30
ML_IN_LITER = 1000
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_IN_LITER

# 4. Вывод красивого результата
print("-" * 40)
print("    🩹  Отчет для пользователя:💊")
print("-" * 40)
print(f"Имя: {user_name}\n"
      f"Возраст: {user_age}лет\n"
      f"Ваш индекс массы тела: {bmi}\n"
      f"Рекомендуемая норма воды: {water_l:.1f}л. в день")
print("-" * 40)
print(" ❤️  Расчет окончен. Будьте здоровы!❤️")
print("-" * 40)
