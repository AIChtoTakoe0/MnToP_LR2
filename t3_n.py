n = int(input("Введите целое неотрицательное число: "))
if not isinstance(n, int) or isinstance(n, bool):
    raise TypeError("n должно быть целым числом")
if n < 0:
    raise ValueError("n должно быть неотрицательным")

result = 1
for i in range(2, n+1):
    result *= i

print(f"Факториал {n} равен {result}")
