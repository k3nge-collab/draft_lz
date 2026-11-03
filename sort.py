import random
# Создаем список из 100 случайных целых чисел от 0 до 1_000_000
random.seed(42)  # Для воспроизводимости результатов
start_list = [random.randint(0, 1_000_000) for _ in range(100)]
print(" Сортировка пузырьком ")
sorted_list_bubble = list(start_list)  # Копируем исходный список
comparisons_bubble = 0
stop_flag = True
iteration_bubble = 1
while stop_flag is True:
    stop_flag = False
    for i in range(0, len(sorted_list_bubble) - 1):
        comparisons_bubble += 1
        if sorted_list_bubble[i] < sorted_list_bubble[i + 1]: # Поменяли знак '>' на '<', чтобы сортировать по убыванию
            swap = sorted_list_bubble[i]
            sorted_list_bubble[i] = sorted_list_bubble[i + 1]
            sorted_list_bubble[i + 1] = swap
            stop_flag = True
    print(f"Итерация {iteration_bubble}: {sorted_list_bubble}")
    iteration_bubble += 1
print(" Сортировка выбором ")
unsorted_list = list(start_list)  # Копируем исходный список
sorted_list_selection = []
comparisons_selection = 0
iteration_selection = 1
while len(unsorted_list) > 0:
    # Инициализируем переменную для поиска максимума (по убыванию)
    max_val = unsorted_list[0]
    for i in range(0, len(unsorted_list)):
        comparisons_selection += 1
        if unsorted_list[i] > max_val:  # Поменяли знак '<' на '>', чтобы искать максимум для сортировки по убыванию
            max_val = unsorted_list[i]
    sorted_list_selection.append(max_val)
    unsorted_list.remove(max_val)
    print(f"Итерация {iteration_selection}: Текущий результат -> {sorted_list_selection}")
    iteration_selection += 1
print("="*50)
print("ИТОГОВЫЕ РЕЗУЛЬТАТЫ:")
print(f"Отсортированный список (Пузырек): {sorted_list_bubble}")
print(f"Отсортированный список (Выбор):   {sorted_list_selection}")
print(f"Количество сравнений (Пузырек):   {comparisons_bubble}")
print(f"Количество сравнений (Выбор):     {comparisons_selection}"
