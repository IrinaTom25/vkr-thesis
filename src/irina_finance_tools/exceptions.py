"""
Собственные исключения для библиотеки finance_tools
"""


class FinanceError(Exception):
    """Базовое исключение для всех ошибок библиотеки"""

    pass


class NegativeAmountError(FinanceError):
    """Ошибка: сумма не может быть отрицательной"""

    pass


class InvalidRateError(FinanceError):
    """Ошибка: процентная ставка должна быть от 0 до 100"""

    pass
