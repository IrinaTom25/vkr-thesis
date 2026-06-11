# irina-finance-tools

Библиотека для финансовых расчётов.

## Установка

```bash
pip install irina-finance-tools
from irina_finance_tools.taxes import calculate_nds_add
from irina_finance_tools.invoice import Invoice

# НДС
print(calculate_nds_add(100, 20))  # 120.0

# Счёт
inv = Invoice()
inv.add_item("Ноутбук", 50000, 1)
print(inv.total(20))  # 60000.0

## Ссылка на пакет

https://pypi.org/project/irina-finance-tools/
