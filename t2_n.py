"""Задача 2. Минимальный элемент списка (ручной ввод, без min()).

Ввод: числа через пробел, окончание — пустая строка.
"""


def parse_line(line: str) -> list[int]:
    """Разбирает строку в список int, пропуская нечисловые токены."""
    result: list[int] = []
    for token in line.split():
        try:
            result.append(int(token))
        except ValueError:
            print(f"  Пропущено (не число): {token!r}")
    return result


def read_numbers() -> list[int]:
    """Читает числа с клавиатуры до пустой строки."""
    numbers: list[int] = []
    print("Вводите числа через пробел. Пустая строка — конец ввода.")
    while True:
        line = input("> ").strip()
        if line == "":
            break
        numbers.extend(parse_line(line))
    return numbers


def find_min(values: list[int]) -> int | None:
    """Возвращает минимальный элемент или None для пустого списка."""
    if not values:
        return None
    minimum = values[0]
    for value in values[1:]:
        if value < minimum:
            minimum = value
    return minimum


if __name__ == "__main__":
    data = read_numbers()
    print(f"Получен список: {data}")
    result = find_min(data)
    if result is None:
        print("Список пуст — минимум не определён.")
    else:
        print(f"Минимум: {result}")
