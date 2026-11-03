import random
# Создаем отсортированный список из 100 уникальных случайных чисел от 0 до 1_000_000
collection = sorted(list(set(random.sample(range(0, 1_000_001), 100))))
# Запрашиваем у пользователя искомое значение
element = int(input("Введите число для поиска: "))
# Линейный поиск
linear_comparisons = 0
for i in range(len(collection)):
  linear_comparisons += 1
  if collection[i] == element:
    break
print("Линейный поиск")
if collection[i] == element:
  print(f"Элемент найден по индексу: {i}")
  print(f"Количество сравнений: {linear_comparisons}")
else:
  print("Элемент не найден.")
# Бинарный поиск 
first = 0
last = len(collection) - 1
index = -1
binary_comparisons = 0
while (first <= last) and (index == -1):
  binary_comparisons += 1
  mid = (first + last) // 2
  if collection[mid] == element:
    index = mid
  else:
    if element < collection[mid]:
      last = mid - 1
    else:
      first = mid + 1
print("Бинарный поиск")
if index != -1:
  print(f"Элемент найден по индексу: {index}")
  print(f"Количество сравнений: {binary_comparisons}")
else:
  print("Элемент не найден.")
