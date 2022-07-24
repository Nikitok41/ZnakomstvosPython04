# Вычислить число pi c заданной точностью d Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import All_functions_for_home_work_dz4 as PF
# import math
# digits_dictionary ={} # создаю словарь выборов округления
# for i in range(1,11):
#     digits_dictionary[i] = 10**-i
# print(f"Choost from 1 - 10 ammount of digits in Pi:\n")
# PF.print_dictionary_in_lines(digits_dictionary)
# digits_d = PF.input_number_examination(text_in_input="\nEnter d : ",case_def=3,min_num=1,max_num=10)
# pi_number = round(math.pi,digits_d)
# print(f"\nPi with {digits_dictionary[digits_d]} digits = {pi_number}")



# Задайте натуральное число N.
# Напишите программу, которая составит список
# простых делителей числа N. (1 - составное число)


# import All_functions_for_home_work_dz4 as PF
# number_N = PF.input_number_examination(text_in_input="Enter N : ",case_def=1)
# def simpl_nums_of_number(number : int ) ->list:
#     list_of_simple_numbers =[]
#     number_to_work = number_N
#     for j in range(2,number_N+1):
#         for i in range(2,number_N+1):
#             if number_to_work % i == 0:
#                 list_of_simple_numbers.append(i)
#                 number_to_work = number_to_work / i
#                 break
#     return list_of_simple_numbers
# ls_of_simpl_mult = simpl_nums_of_number(number_N)
# print(f"In number {number_N} list of siple multipliers are -> {ls_of_simpl_mult} -> {set(ls_of_simpl_mult)}")


# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.


# from All_functions_for_home_work_dz4 import fibonachi_from_minus_to_plus
# list_of_fibonacci = fibonachi_from_minus_to_plus(8)
# print(f"Fibbonaci : {list_of_fibonacci}")
# def list_without_duble(list_of_numbers : list) ->list:
#     """Затягивает список - и выводит новый, с непвторяющимеся эллементами
#     Args:
#         list_of_numbers (list): Изначальный список, в котором происходит поиск эллементов
#     Returns:
#         list: Новый список без повторений
#     """
#     new_list =[list_of_numbers[0]]
#     for i in list_of_numbers:
#         count = 1
#         for j in new_list:
#             if i == j:
#                 count +=1
#         if count == 1:
#             new_list.append(i)
#     return new_list
# # count
# def list_with_no_(list_of_numbers : list) ->list:
#     new_list = []
#     for i in list_of_numbers:
#         if list_of_numbers.count(i) == 1:
#             new_list.append(i)
#     return new_list
# print(f"Without repetitions : {list_with_no_(list_of_fibonacci)}")



# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и вывести на экран.


# from random import randint
# import itertools
#
# k = randint(2, 7)
#
# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios
#
# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')
#
#
# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)