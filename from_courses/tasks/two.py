"""
Напишите функцию anonymous_filter, используя синтаксис анонимных функций,
которая принимает строковый аргумент и возвращает значение True,
сли количество русских букв я не меньше 23 (регистр буквы неважен) и False в
противном случае.

Примечание. Вызывать анонимную функцию не нужно. Только дописать ее код.

Sample Input 1:
print(anonymous_filter('Я - последняя буква в алфавите!'))
Sample Output 1:
False
Sample Input 2:
print(anonymous_filter
('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))
Sample Output 2:
True
"""

anonymous_filter = lambda text: str(text).lower().count('я') > 23
print(anonymous_filter('Я - последняя буква в алфавите!'))

print(anonymous_filter(
    'яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!')
)
