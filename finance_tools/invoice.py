"""
Модуль для работы со счетами (Invoice)
"""

from typing import Dict, List

from .exceptions import InvalidRateError, NegativeAmountError


class Invoice:
    """
    Класс для представления счёта.
    """

    def __init__(self):
        """Создаёт пустой счёт."""
        self._items: List[Dict[str, float]] = []

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """
        Добавить позицию в счёт.
        """
        if price < 0:
            raise NegativeAmountError(f"Цена не может быть отрицательной: {price}")
        if quantity < 0:
            raise NegativeAmountError(
                f"Количество не может быть отрицательным: {quantity}"
            )

        self._items.append({"name": name, "price": price, "quantity": quantity})

    def subtotal(self) -> float:
        """Рассчитать сумму без налогов."""
        return sum(item["price"] * item["quantity"] for item in self._items)

    def tax(self, rate: float) -> float:
        """Рассчитать сумму налога."""
        if not 0 <= rate <= 100:
            raise InvalidRateError(f"Ставка налога должна быть от 0 до 100: {rate}")
        return self.subtotal() * rate / 100

    def total(self, tax_rate: float = 20) -> float:
        """Рассчитать итоговую сумму с налогом."""
        return self.subtotal() + self.tax(tax_rate)

    def __len__(self) -> int:
        """Количество позиций в счёте."""
        return len(self._items)
