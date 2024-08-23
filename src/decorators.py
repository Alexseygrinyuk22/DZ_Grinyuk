from time import time
from functools import wraps
def log(filename):
    """Декоратор который логирует вызов функции и ее результат в файл или консоль"""

    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                time_1 = time()
                result = func(*args, *kwargs)
                time_2 = time
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function start - {time_1} \nmy_functions ok \nmy_functions stop - {time_2}")
                else:
                    print(f"my_function start - {time_1} \nmy_functions ok \nmy_functions stop - {time_2}")
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function error: {e}.Inputs: {args}, {kwargs}")
                else:
                    print(f"my_function error: {e}.Inputs: {args}, {kwargs}")
                raise
            return result
        return wrapper
    return timer(func)


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция складывает два числа"""
    return x + y


my_function(1, 2)
