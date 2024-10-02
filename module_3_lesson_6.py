# Устанавливаем счётчик
count = 0

# Рекурсивная функция для подсчёта значений
def calculate_structure_sum(*values):

  # Обращаемся к глобальной переменной
  global count

  # Циклом перебираем все элементы в переданных данных
  for element in values:

    # Если элемент является целым числом, то увеличиваем значение счётчика на значение этого числа
    if isinstance(element, int):
      count += element

    # Если элемент является строкой, то увеличиваем значение счётчика на длину этой строки
    if isinstance(element, str):
      count += len(element)

    # Если элемент является списком, то элементы списка отдаём на обработку функции
    if isinstance(element, list) and len(element) != 0:
      calculate_structure_sum(*element)

    # Если элемент является кортежем, то элементы кортежа отдаём на обработку функции
    if isinstance(element, tuple) and len(element) != 0:
      calculate_structure_sum(*element)

    # Если элемент является множеством, то элементы множества отдаём на обработку функции
    if isinstance(element, set) and len(element) != 0:
      calculate_structure_sum(*element)

    # Если элемент является словарём, то элементы словаря отдаём на обработку функции
    # Сначала ключи, потом значения ключей
    if isinstance(element, dict) and len(element) != 0:
      calculate_structure_sum(*element.keys())
      calculate_structure_sum(*element.values())

  # Возвращаем полученный результат
  return count

# исходные данные
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Отдаём исходные данные на обработку функции
result = calculate_structure_sum(*data_structure)

# Выводим полученный результат
print(result)
