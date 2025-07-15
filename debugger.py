'''
в нас є  список [1, 2, 3, 4, 5, 6, 7, 8, 9] / потрібно написати функцію, яка буде проходити по цьому списку та виводити
лише не парні числа

'''


def is_even(number: int)->bool:
    '''
    Function that receives numbers and returns True if the number is even
    :param number: int
    :return: bool
    '''
    return  number % 2 == 0


print(is_even(5))

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_odd_numbers(lst: list[int]):
    '''
    a function that receives a list of numbers and prints out the odd numbers
    :param lst: list
    :return: None
    '''
    for chars in lst:  #пройтися по усім елементам списку
        if chars % 2 != 0:  # перевірка на непарність
            print(chars, end=' ')  # якщо непарні друкуємо


print_odd_numbers(list)
