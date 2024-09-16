#* Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter.
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел

# Входной список может быть подан и иначе
lst_in = [1,2,3,4,22,234,24] # ----> [22, 24]

# list comprehension
# lst_out = [el for el in lst_in if 9 < el < 100]

lst_out = list(filter(lambda el: 9 < el < 100, lst_in))

print(lst_out)