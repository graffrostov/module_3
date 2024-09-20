"""
Вам необходимо написать 3 функции:
[]Функция count_calls подсчитывающая вызовы остальных функций.
[]Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
[]Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
Пункты задачи:
[x]Создать переменную calls = 0 вне функций.
[x]Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
[]Создать функцию string_info с параметром string и реализовать логику работы по описанию.
[]Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
[]Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
[]Вывести значение переменной calls на экран(в консоль).
"""

# создаём счётчик вызова функций
calls = 0

# Функция счётчик. При вызове увеличивает значение счётчика на единицу.
def count_calls():
    global calls
    calls += 1

# принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре
def string_info(work_string = ''):
    string_cortage = (len(work_string), work_string.upper(), work_string.lower())
    count_calls()
    return string_cortage

# принимает два аргумента: строку и список, и возвращает
# True, если строка находится в этом списке, False - если отсутствует.
def is_contains(string = '', list_to_search = []):
    # string.casefold()
    result = string.lower() in (item.lower() for item in list_to_search)
    count_calls()
    return result

# Печатаем результаты.
print(string_info('Capybara'))
print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print('Обращений к функциям:' ,calls)
