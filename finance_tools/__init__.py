"""
finance_tools — библиотека для финансовых расчётов.
"""

from .exceptions import FinanceError, InvalidRateError, NegativeAmountError
from .invoice import Invoice
from .loan import LoanCalculator
from .taxes import (
    calculate_margin,
    calculate_markup,
    calculate_nds_add,
    calculate_nds_extract,
    net_salary,
)

__all__ = [
    "FinanceError",
    "NegativeAmountError",
    "InvalidRateError",
    "Invoice",
    "LoanCalculator",
    "calculate_nds_add",
    "calculate_nds_extract",
    "calculate_margin",
    "calculate_markup",
    "net_salary",
]
