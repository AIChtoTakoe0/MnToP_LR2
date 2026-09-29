VOWELS_RU = set("аеёиоуыэюя")
VOWELS_EN = set("aeiou")


def count_vowels(text: str, alphabet: str = "ru") -> int:
    if alphabet not in {"ru", "en", "both"}:
        raise ValueError(f"Неизвестный алфавит: {alphabet}")
    text_lower = text.lower()
    if alphabet == "ru":
        vowels = VOWELS_RU
    elif alphabet == "en":
        vowels = VOWELS_EN
    else:
        vowels = VOWELS_RU | VOWELS_EN

    return sum(1 for ch in text_lower if ch in vowels)


if __name__ == "__main__":
    text = input("Введите строку: ")
    print(f"Русских гласных: {count_vowels(text, 'ru')}")
    print(f"Английских гласных: {count_vowels(text, 'en')}")
