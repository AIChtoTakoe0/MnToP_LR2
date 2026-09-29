"""Задача 4. Частота слов в текстовом файле (путь вводит пользователь)."""
import re
from collections import Counter
from pathlib import Path


def word_frequency(path: Path) -> Counter:
    """Возвращает счётчик слов для файла (UTF-8, регистр игнорируется)."""
    text = path.read_text(encoding="utf-8").lower()
    words = re.findall(r"[а-яёa-z]+", text)
    return Counter(words)


def print_top(counter: Counter, limit: int = 10) -> None:
    """Выводит top-N слов по убыванию частоты."""
    for word, count in counter.most_common(limit):
        print(f"{word:>15} : {count}")


def ask_path() -> Path | None:
    """Запрашивает абсолютный путь к файлу до успешного ввода."""
    print("Введите абсолютный путь к текстовому файлу.")
    print("Пустая строка — выход.")
    while True:
        raw = input("> ").strip().strip('"').strip("'")
        if raw == "":
            return None
        path = Path(raw)
        if not path.is_absolute():
            print(f"  Нужен абсолютный путь. Пример: {Path.cwd() / 'sample.txt'}")
            continue
        if not path.is_file():
            print(f"  Файл не найден: {path}")
            continue
        return path


if __name__ == "__main__":
    file_path = ask_path()
    if file_path is None:
        print("Отменено пользователем.")
    else:
        freq = word_frequency(file_path)
        print(f"Файл: {file_path}")
        print(f"Всего уникальных слов: {len(freq)}")
        print_top(freq, limit=10)
