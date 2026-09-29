"""Задача 5. Игра «Угадай число»."""
import random


def play(low: int = 1, high: int = 100) -> None:
    """Запускает игру: угадать число в диапазоне [low, high]."""
    secret = random.randint(low, high)
    attempts = 0
    print(f"Я загадал число от {low} до {high}. Попробуй угадать!")

    while True:
        raw = input("Твой вариант: ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("Это не число, попробуй ещё раз.")
            continue

        attempts += 1

        if guess < secret:
            print("Больше.")
        elif guess > secret:
            print("Меньше.")
        else:
            print(f"Угадал! Число {secret}, попыток: {attempts}.")
            return


if __name__ == "__main__":
    play()
