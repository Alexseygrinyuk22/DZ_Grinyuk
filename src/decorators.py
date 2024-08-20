def log(filename):
    """Декоратор который логирует вызов функции и ее результат в файл или консоль"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function ok")
                else:
                    print(f"my_function ok")
            except Exceptoin as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function error: {e}.Inputs: {args}, {kwargs}")
                else:
                    print(f"my_function error: {e}.Inputs: {args}, {kwargs}")
                raise
            return result


def printing(func):
    """Декоратор который показывает начало и конец функции"""

    def wrapper(*args, **kwargs):
        print(f"Функция {func} запуск")
        result = func(*args, **kwargs)
        print(f"Функция {func} окончание")
        return result

    return wrapper


@printing
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
