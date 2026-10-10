def add_numbers(a: float, b: float) -> float:
    """
    Сложение двух чисел

    Args:
        a (float): Первое число для сложения
        b (float): Второе число для сложения

    Returns:
        float: Итоговый зрезультат сложения

    Raises:
        ValueError: Если введены данные неправильного формата.

    Example:
        >> add_numbers(2, 2)
        4
    """
    return a + b

def divide(a, b):
    """
    Деление двух чисел

    Args:
        a (int): Делимое
        b (int): Делитель

    Returns:
        int: Итоговый зрезультат деления/частное

    Raises:
        ValueError: Если введены данные неправильного формата.

    Example:
        >> divide(2, 2)
        1
    """
    if b == 0:
        return 'На ноль делить нельзя'
    else:
        return a / b