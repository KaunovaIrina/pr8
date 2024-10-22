while True:
 a_str = input("Введите первое число: ")
 b_str = input("Введите второе число: ")

 # Проверка на корректность ввода (только числа)
 if a_str.replace("-", "").isdigit() and b_str.replace("-", "").isdigit():def input_number():
 """
 Функция для ввода числа с проверкой на корректность.
 """
 while True:
  number_str = input("Введите число: ")
  if number_str.lower() in ("stop", "end"):
   return None

  # Проверка на корректность ввода (только числа)
  if number_str.replace("-", "").isdigit():
   number = float(number_str)
   if number.is_integer():
    return int(number)
   else:
    print("Ошибка: Введите целое число или 'stop'/'end' для завершения.")
  else:
   print("Ошибка: Введите число или 'stop'/'end' для завершения.")

def main():
 """
 Основная функция программы.
 """
 numbers = []
 while True:
  number = input_number()
  if number is None:
   break
  numbers.append(number)

 sum_of_numbers = 0
 if numbers:
  print("Введенные числа:", numbers)
  for number in numbers:
   sum_of_numbers += number
  print("Сумма чисел:", sum_of_numbers)
 else:
  print("Не введено ни одного числа.")

