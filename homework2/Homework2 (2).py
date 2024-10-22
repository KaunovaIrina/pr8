while True:
 num1_str = input("Введите первое число: ")
 num2_str = input("Введите второе число: ")

 # Проверка на корректность ввода (допускаются отрицательные числа)
 if num1_str.replace("-", "").isdigit() and num2_str.replace("-", "").isdigit():
  num1 = int(num1_str)
  num2 = int(num2_str)
  sum = num1 + num2
  print("Сумма чисел:", sum)
 else:
  print("Ошибка: ввод должен содержать только целые числа.")