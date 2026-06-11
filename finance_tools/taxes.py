"""
Модуль для расчёта налогов и финансовых показателей
"""

from .exceptions import InvalidRateError, NegativeAmountError


def calculate_nds_add(amount: float, rate: float = 20) -> float:
    """
    Добавить НДС к сумме.
    """
    if amount < 0:
        raise NegativeAmountError(f"Сумма не может быть отрицательной: {amount}")
    if not 0 <= rate <= 100:
        raise InvalidRateError(f"Ставка НДС должна быть от 0 до 100: {rate}")

    return amount * (1 + rate / 100)


def calculate_nds_extract(amount_with_nds: float, rate: float = 20) -> float:
    """
    Выделить НДС из суммы.
    """
    if amount_with_nds < 0:
        raise NegativeAmountError(
            f"Сумма не может быть отрицательной: {amount_with_nds}"
        )
    if not 0 <= rate <= 100:
        raise InvalidRateError(f"Ставка НДС должна быть от 0 до 100: {rate}")

    return amount_with_nds * rate / (100 + rate)


def calculate_margin(cost: float, revenue: float) -> float:
    """
    Рассчитать маржу (прибыль / выручка).
    """
    if revenue == 0:
        return 0.0
    return ((revenue - cost) / revenue) * 100


def calculate_markup(cost: float, revenue: float) -> float:
    """
    Рассчитать наценку (прибыль / себестоимость).
    """
    if cost == 0:
        return 0.0
    return ((revenue - cost) / cost) * 100


def net_salary(gross_salary: float, tax_rate: float = 13) -> float:
    """
    Рассчитать чистую зарплату после налога.
    """
    if gross_salary < 0:
        raise NegativeAmountError(
            f"Зарплата не может быть отрицательной: {gross_salary}"
        )
    if not 0 <= tax_rate <= 100:
        raise InvalidRateError(f"Ставка налога должна быть от 0 до 100: {tax_rate}")

    return gross_salary * (1 - tax_rate / 100)
