"""
Модуль для расчёта кредитов
"""

from .exceptions import InvalidRateError, NegativeAmountError


class LoanCalculator:
    """
    Класс для расчёта аннуитетных платежей по кредиту.
    """

    def __init__(self, amount: float, rate: float, term: int):
        """
        Инициализация кредита.
        """
        if amount < 0:
            raise NegativeAmountError(
                f"Сумма кредита не может быть отрицательной: {amount}"
            )
        if not 0 <= rate <= 100:
            raise InvalidRateError(f"Ставка должна быть от 0 до 100: {rate}")
        if term <= 0:
            raise ValueError(f"Срок кредита должен быть положительным: {term}")

        self.amount = amount
        self.rate = rate
        self.term = term
        self._monthly_rate = rate / 100 / 12

    def annuity_payment(self) -> float:
        """Рассчитать ежемесячный аннуитетный платёж."""
        if self.rate == 0:
            return self.amount / self.term

        rate = self._monthly_rate
        factor = (rate * (1 + rate) ** self.term) / ((1 + rate) ** self.term - 1)
        return self.amount * factor

    def total_payment(self) -> float:
        """Рассчитать общую сумму выплат по кредиту."""
        return self.annuity_payment() * self.term

    def total_interest(self) -> float:
        """Рассчитать общую переплату по кредиту."""
        return self.total_payment() - self.amount
