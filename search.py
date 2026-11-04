import random
unique_set = set()

while len(unique_set) < 100:
    unique_set.add(random.randint(0, 1_000_000))
collection = sorted(list(unique_set))
print("Отсортированный список из 100 случайных целых чисел:")
print(collection)
element = random.choice(collection)                              # Берем случайный элемент, который точно есть в нашей коллекции
print("Мы будем искать число: " + str(element))

schetchik_l = 0                                                  # Счетчик сравнений
index_l = -1
for i in range(len(collection)):
    schetchik_l = schetchik_l + 1                                # Считаем проверку
    if collection[i] == element:
        index_l = i                                              # Запомнили индекс найденного элемента
        break

schetchik_b = 0                                                  # Счетчик сравнений
first = 0
last = len(collection) - 1
index_b = -1

while (first <= last) and (index_b == -1):
    schetchik_b = schetchik_b + 1                                # Считаем проверку
    
    mid = (first + last) // 2
    if collection[mid] == element:
        index_b = mid
    else:
        if element < collection[mid]:
            last = mid - 1
        else:
            first = mid + 1
print("=================================================")
print("ИТОГИ ЛИНЕЙНОГО ПОИСКА")
print("=================================================")
if index_l != -1:
    print("Элемент найден под индексом: " + str(index_l))
    print("Всего проверок сделано: " + str(schetchik_l))
else:
    print("Элемент не найден в списке!")

print("=================================================")
print("ИТОГИ БИНАРНОГО ПОИСКА")
print("=================================================")
if index_b != -1:
    print("Элемент найден под индексом: " + str(index_b))
    print("Всего проверок сделано: " + str(schetchik_b))
else:
    print("Элемент не найден в списке!")
print("=================================================")
