"""
Главный модуль проекта
"""

from core.processing import process_data, get_length


def main():
    """
    Главная функция
    """
    input_data = "example"
    
    result = process_data(input_data)
    length = get_length(input_data)
    
    print(f"Исходная строка: {input_data}")
    print(f"Результат обработки: {result}")
    print(f"Длина строки: {length}")


if __name__ == "__main__":
    main()