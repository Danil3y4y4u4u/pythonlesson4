#user_input = input("Ввудите что нибудь: ")
#if user_input:
#    print("Ok")

#a = float(input("Введите ширину форточки (a): "))
#b = float(input("Введите высоту форточки (b): "))
#d = float(input("Введите диаметр головы (d): "))
#
#required_size = d + 2
#
#if a >= required_size and b >= required_size:
#    print("Да, Вася сможет высунуть голову.")
#else:
#    print("Нет, зазор недостаточен или форточка мала.")


x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = int(input("Введите третье число: "))

print("Максимальное значение:", max(x, y, z))
print("Минимальное значение:", min(x, y, z))