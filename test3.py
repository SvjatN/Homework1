"""
Задано чотирицифрове натуральне число. 
Знайти добуток цифр цього числа.
Записати число в реверсному порядку.
Посортувати цифри, що входять в дане число
  
"""
import functools

number = 9845
product_of_number = functools.reduce((lambda iter ,a: iter*a ), [int(i) for i in str(number)])
print("product of number  = " + str(product_of_number))

reverse_number = list(str(number))
reverse_number.reverse()
reverse_number = "".join(reverse_number)
print("reverse number  = " + reverse_number)

sort_number = list(str(number))
sort_number.sort()
sort_number = "".join(sort_number)
print("sort number  = " + sort_number)

