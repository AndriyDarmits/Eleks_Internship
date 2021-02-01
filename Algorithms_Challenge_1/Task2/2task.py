import os
# запитуємо індекс елемента
index_of_element = int(input("Введіть індекс елемента: "))


def fibonacci_by_index(index):
    if index in (1, 2):
        return 1
    return fibonacci_by_index(index - 1) + fibonacci_by_index(index - 2)


print(fibonacci_by_index(index_of_element))
os.system("pause")