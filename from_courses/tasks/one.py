"""
Реализуйте функцию custom_filter(), которая на вход принимает список some_list,
с любыми типами данных, находит в этом списке целые числа, отбирает из них те,
что делятся нацело на 7, суммирует их, а затем проверяет превышает э
та сумма 83 или нет. Если НЕ превышает - функция должна вернуть True,
если превышает - False.

Примечание. В тестирующую систему сдайте программу, содержащую только
необходимую функцию custom_filter(), но не код, вызывающий ее.

Sample Input 1:
some_list = [7, 14, 28, 32, 32, 56]

print(custom_filter(some_list))
Sample Output 1:
False

Sample Input 2:
some_list = [7, 14, 28, 32, 32, '56']

print(custom_filter(some_list))
Sample Output 2:
True
"""


def custom_filter(some_list: list) -> bool:
    some_list = [
        val for val in some_list if isinstance(val, int) and val % 7 == 0
    ]
    return True if sum(some_list) < 83 else False


some_list = [7, 14, 28, 32, 32, 56]
print(custom_filter(some_list))