x = []
n = 1
while True:
    value = input(f"Введіть значення №{n} для списку: ")
    x.append(value)
    answer = input("Продовжуємо додавати? Y/N: ").lower()
    if answer != "y":
        break
    n += 1
print(f"Список складається із {n} Значень: {x}")

y = int(input("Введіть число, на яке ви б бажали розбити список: "))

def dilemo_list(y):
    if len(x) % y == 0:
        result = [x[i:i+len(x)//y] for i in range(0,len(x),len(x)//y)]
        print(*result, sep=",")
    else:
        print(f"Нажаль список який ви ввели, що складається з {len(x)} значень,\nне може бути рівно поділиний на {y} рівні менші списки")
        
dilemo_list(y)
