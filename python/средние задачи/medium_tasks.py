# 1.Создайте программу, которая проверяет,
#  является ли введенное пользователем число четным или нечетным, и выводит соответствующее сообщение.

num = int(input("Введите число: "))
if num % 2 == 0:
    print(f'Число {num} чётное')
else:
    print(f'Число {num} нечётное')

# 2.Реализуйте программу, которая определяет, 
# является ли введенная пользователем строка палиндромом 
# (читается одинаково слева направо и справа налево). Выведите соответствующее сообщение.


string = input('Введите строку: ')

middle_index = len(string)//2
if len(string) % 2 == 0:
    second_part = string[middle_index: ]
else:
    second_part = string[middle_index + 1: ]


# if string[0: middle_index] == ''.join(reversed(second_part)): 
#     print('Это палиндром')
# else:
#     print('Это не палидром')

# 3.Реализуйте программу, которая определяет, 
# является ли заданное число простым (имеет только два делителя: 1 и само число). 
# Выведите соответствующее сообщение.
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# print(is_prime(8))
# print(is_prime(17))


# 4.Реализуйте программу, которая определяет, 
# является ли заданная дата корректной (). Выведите соответствующее сообщение.
# Дата дана в формате “20.01.2002”

# import time

def check_valid_date(date):
    try: 
        time.strptime(date, "%d.%m.%Y")
        return True
    except ValueError:
        return False

date_str = input("Введите дату: ")

if check_valid_date(date_str):
    print("Date is correct")
else:
    print('Date is not correct')


# 5.Напишите программу для нахождения всех совершенных чисел (чисел, равных сумме своих делителей, 
# исключая само число) в заданном диапазоне. Диапазон от 0 до 1000

num = int(input('Please enter a number in range {"1: 1000"}: '))

if num not in range(2, 1001):
    print(f'{num} is out of range')
else:
    perfect_nums = []
    for i in range(1, num + 1):
        div_sum = 0
        for j in range(1, i):
            if i % j == 0:
                div_sum += j
        if div_sum == i:
            perfect_nums.append(i)

    if perfect_nums: 
        print(f'Perfect numbers are: {perfect_nums}')
    else: 
        print(f'There is no perfect numbers')

#6.Реализуйте программу для проверки, является ли заданное число 
# числом Фибоначчи (число, которое является членом последовательности Фибоначчи). Заданное число 25
def is_fibonacci(num):
    if num == 0 or num == 1: 
        return True
    
    fib1, fib2 = 0, 1  
    while fib2 < num:  
        fib1, fib2 = fib2, fib1 + fib2  
        
    return fib2 == num 

print(is_fibonacci(25))

# 7.Напишите программу, которая определяет, является ли заданное число совершенным числом 
# (число, равное сумме своих делителей, исключая само число). Выведите сообщение с результатом.

num = int(input('Please enter a number: '))

if num < 2:
    print(f'{num} is not perfect number')
else:
    div_sum = sum(i for i in range(1, num) if num % i == 0 )
    if div_sum == num:
        print(f'{num} is a perfect number')
    else: 
        print(f'{num} is not perfect number')




# 8.Создайте программу, которая определяет, в какой сезон года попадает заданная дата (месяц и день). 

date_str = input('Please, enter the date in format {"dd.mm"}: ')
day, month = map(int, date_str.split('.'))
if day not in range(1, 32) or month not in range(1, 13):
    print("The date is not valid")
elif (month == 12 and day >= 21) or month in range(1, 3) or (month == 3 and day <= 19):
    print("Winter")
elif (month == 3 and day >= 20) or month in range(4, 6) or (month == 6 and day <= 20):
    print("Spring")
elif (month == 6 and day >= 21) or month in range(7, 9) or (month == 9 and day <= 22):
    print('Summer')
elif (month == 9 and day >= 23) or month in range(10, 12) or (month == 12 and day <= 20):
    print("Autumn")
   

