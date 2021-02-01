import os.path

while True:
    # запитуємо шлях до файлу
    file_path = input("Введіть шлях до файлу: ")

    # перевіряємо, чи файл існує
    if os.path.exists(file_path):

        # відкриваємо файл для читання та зчитуємо інформацію
        with open(file_path, "r", encoding="utf-8") as f:
            text_array = [line.strip() for line in f]
            print(text_array)

        # запитуємо шлях для вихідного файлу
        revert_file_path = input("Введіть шлях до вихідного файлу: ")

        # відкриваємо файл для запису та записуємо дані у зворотньому порядку
        with open(revert_file_path, "w", encoding="utf-8") as revert_file:
            for line in text_array:
                revert_file.write(line[::-1] + '\n')

        exit()
    else:
        print("Такого файлу не існує(")
