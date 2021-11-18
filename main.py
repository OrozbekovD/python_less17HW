def decor(func):
    def wrapper(arg):
        print('Привет')
        func(arg)
        print('Конец функции')

    return wrapper


@decor
def sum(a):
    a = a + 2
    print(a)


sum(1)
