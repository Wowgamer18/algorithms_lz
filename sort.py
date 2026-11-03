import random
spisok = []
for _ in range(100):
    randomnoe_chislo = random.randint(0, 1000000)
    spisok.append(randomnoe_chislo)
print(spisok)

p = list(spisok)
schetchik_p = 0
dlina_spiska = len(p)

print("\n                         --- СОРТИРОВКА ПУЗЫРЬКОМ ---")
for i in range(dlina_spiska):
    for b in range(0, dlina_spiska - i - 1):
        schetchik_p = schetchik_p + 1             # Сделали сравнение — увеличили счетчик
        if p[b] < p[b + 1]:                       # Если левый элемент меньше правого, меняем их местами для убывания
            z = p[b]
            p[b] = p[b + 1]
            p[b + 1] = z
    print(f"КРУГ СОРТИРОВКИ № {i + 1}. Список выглядит сейчас так: {p}")

v = list(spisok)
schetchik_v = 0

print("\n                         --- СОРТИРОВКА ВЫБОРОМ ---")
for i in range(dlina_spiska):
    index_max = i                                 # Временно считаем, что текущий элемент с индексом i — самый большой
    for b in range(i + 1, dlina_spiska):          # Бежим по оставшейся части списка и ищем элемент, который еще больше
        schetchik_v = schetchik_v + 1             # Сделали сравнение — увеличили счетчик
        if v[b] > v[index_max]:
            index_max = b                         # Запомнили индекс нового самого большого числа
    z = v[i]                                      # Меняем местами начальный элемент i и найденный максимальный элемент
    v[i] = v[index_max]
    v[index_max] = z
    print(f"КРУГ СОРТИРОВКИ № {i + 1}. Список выглядит сейчас так: {v}")
print("=================================================")
print("Последний Круг Сортировки")
print("=================================================")
print(f"Отсортированный список (Пузырек): {p}")
print(f"Отсортированный список (Выбором): {v}")
print("--------------------------------------------------")
print(f"Количество сравнений в Сортировке Пузырьком: {schetchik_p}")
print(f"Количество сравнений в Сортировке Выбором:  {schetchik_v}")
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")