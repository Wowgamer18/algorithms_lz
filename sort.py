import random
spisok = []
for _ in range(100):
    randomnoe_chislo = random.randint(0, 1_000_000)
    spisok.append(randomnoe_chislo)
print(spisok)

p = list(spisok)
schetchik_p = 0
nomer_kruga_p = 0

print("                         ---=== СОРТИРОВКА ПУЗЫРЬКОМ ===---")
stop_flag = True
while stop_flag is True:
    stop_flag = False
    nomer_kruga_p = nomer_kruga_p + 1          # Считаем круги для вывода на экран
    for a in range(0, len(p) - 1):
        schetchik_p = schetchik_p + 1          # Сделали проверку чисел
        if p[a] < p[a + 1]:                    # Знак < делает сортировку по убыванию (маленькие числа уходят вправо)
            z = p[a]
            p[a] = p[a + 1]
            p[a + 1] = z
            stop_flag = True
    print("КРУГ СОРТИРОВКИ № " + str(nomer_kruga_p) + ". Список выглядит сейчас так: " + str(p))
unsorted_list = list(spisok)                  # Исходный неотсортированный список
b = []                                        # Сюда будем складывать самые большие числа по очереди
schetchik_v = 0
nomer_kruga_v = 0

print("                         ---=== СОРТИРОВКА ВЫБОРОМ ===---")
while len(unsorted_list) > 0:
    nomer_kruga_v = nomer_kruga_v + 1
    max = unsorted_list[0]                # Берем самое первое число за текущий максимум
    for i in range(0, len(unsorted_list)):    # Ищем, есть ли число еще больше во всем остатке списка
        schetchik_v = schetchik_v + 1
        if unsorted_list[i] > max:        # Знак > ищет максимум для сортировки по убыванию
            max = unsorted_list[i]
    b.append(max)                         # Добавляем найденный максимум в наш чистый отсортированный список
    unsorted_list.remove(max)             # Удаляем этот максимум из старого списка, чтобы не искать его снова
    print("КРУГ СОРТИРОВКИ № " + str(nomer_kruga_v) + ". Список выглядит сейчас так: " + str(b))
print("=================================================")
print("Последний Круг Сортировки")
print("=================================================")
print(f"Отсортированный список (Пузырек): {p}")
print(f"Отсортированный список (Выбором): {b}")
print("--------------------------------------------------")
print(f"Количество сравнений в Сортировке Пузырьком: {schetchik_p}")
print(f"Количество сравнений в Сортировке Выбором:  {schetchik_v}")
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
