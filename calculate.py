import circle
import square

figs = ['circle', 'square']  # Доступные фигуры
funcs = ['perimeter', 'area']  # Доступные функции
sizes = {}  # Словарь для хранения размеров фигур

def calc(fig, func, size):
    """
    Вычисляет и выводит значение периметра или площади заданной фигуры.

    Параметры:
    fig (str): Название фигуры ('circle' или 'square').
    func (str): Название функции ('perimeter' или 'area').
    size (list): Список параметров для функции.

    Исключения:
    AssertionError: Если fig не в списке доступных фигур или func не в списке доступных функций.
    """
    assert fig in figs
    assert func in funcs

    # Вызываем нужную функцию из модуля фигуры с передачей параметров
    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    # Запрашиваем у пользователя ввод фигуры
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    # Запрашиваем у пользователя ввод функции
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    # Запрашиваем размеры фигуры
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

    # Вызываем функцию для вычисления результата
    calc(fig, func, size)
