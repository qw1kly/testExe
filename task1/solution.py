def strict(func):
    def wrapper(*args, **kwargs):
        if func.__annotations__['return'] == type(args[0]) and func.__annotations__['return'] == type(args[1]):
            return func(*args, **kwargs)
        raise TypeError
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(2, 3)) # ---> 5

#print(sum_two("123", 90)) # ---> Typeerror

#print(sum_two(True, 0)) # ---> Typeerror

#print(sum_two(2.3, 2.9)) # ---> 5.2(Если изменить аннотацию) иначе также Typeerror