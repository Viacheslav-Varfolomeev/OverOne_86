# 8_1

# city_capital = {'Россия': 'Москва',
#         'Украина': 'Киев',
#         'Италия': 'Рим',
#         'Испания': 'Мадрид',
#         'Болгария': 'София'
#         }
# city_capital_1 = input('Введите столицу какой страны вы хотите узнать: ').title()
# for key in city_capital:
#     if key == city_capital_1:
#         print(f'{city_capital_1} - столица {city_capital[key]}')

# 8_2
ls_1 = [i for i in range((int(input('Введите первое число: '))),
                         ((int(input('Введите конечное число: '))) + 1))]
ls_2 = [(input(f'Введите значение  {i + 1} ключа: ').lower()) for i in range(len(ls_1))]

dict_1 = {key: value for key, value in zip(ls_1, ls_2)}
for key in range(len(dict_1) + 1):
    if key % 2 != 0:
        del dict_1[key]
print(dict_1)
