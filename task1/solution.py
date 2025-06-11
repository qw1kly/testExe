def strict(func):
    def wrapper(*args, **kwargs):
        if func.__annotations__['return'] == type(args[0]) and func.__annotations__['return'] == type(args[1]):
            return func(*args, **kwargs)
        raise TypeError
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b


assert sum_two(2, 3) == 5

assert sum_two("123", 90) == TypeError

assert sum_two(True, 0) == TypeError

assert sum_two(2.3, 2.9) == 5.2 #Не та аннотация в функции
