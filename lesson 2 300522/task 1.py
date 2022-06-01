# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать
# функцию type() для проверки типа. Элементы списка можно не запрашивать у
# пользователя, а указать явно, в программе.

str_ex = "Hello"
int_ex = 23
float_ex = 1.2
complex_ex = complex(5, 6)
bool_ex = False
list_ex = [1, 2, {"a": 1, "b": 2}]
tuple_ex = ("world", [10, 9])
set_ex = {"A", "B"}
dict_ex = {"user": "Вася", "age": 24}
byte_ex = b'text'
bytearray_ex = bytearray(b"some text")
mixed_list = [str_ex, int_ex, float_ex, complex_ex, bool_ex, list_ex, tuple_ex,
              set_ex, dict_ex, None, byte_ex, bytearray_ex]
for ind, item in enumerate(mixed_list):
    print(ind, type(item))
