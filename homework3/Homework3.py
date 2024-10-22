def draw_square(size):
 """Рисует квадрат из символов "*" заданного размера."""
 if size.isdigit() and int(size) > 0:
  size = int(size)
  for _ in range(size):
   print("*" * size)
 else:
  print("Ошибка: Размер квадрата должен быть целым числом больше 0.")

while True:
 size = input("Введите размер квадрата (целое число больше 0): ")
 draw_square(size)
 if size.isdigit() and int(size) > 0:
  break # Выходим из цикла после успешного рисования
