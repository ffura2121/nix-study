import random

for el in range(1,101):
    result = random.randint(1,1000)
    print(f"№{el} - {result}")
    if result == 777:
        print(f"Число 777 було знайдено на {el} повторі")
        break
if result != 777:
    print("Число 777 не було знайдено з 100 повторів")

