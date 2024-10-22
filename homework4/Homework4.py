while True:
 a_str = input("Введите первое число: ")
 b_str = input("Введите второе число: ")

 # Проверка на корректность ввода (только числа)
 if a_str.replace("-", "").isdigit() and b_str.replace("-", "").isdigit():
  a = float(a_str)
  b = float(b_str)

  # Проверка на целые числа
  if a.is_integer() and b.is_integer():
   a = int(a)
   b = int(b)

   # Проверка на корректный ввод
   if a > b:
    a, b = b, a # Меняем местами, если a больше b
   print("Целые числа между", a, "и", b, ":")
   for i in range(a + 1, b):
    print(i, end=" ")
   print()
   break # Выходим из цикла после успешного вывода
  else:
   print("Ошибка: Введены нецелые числа.")
 else:
  print("Ошибка: Введены некорректные данные.")

