##########################__ЗАДАНИЕ_1__########################################
import threading
import random


class ThreadSafeList:
    def __init__(self):
        self.list = []
        self.lock = threading.Lock()
        self.list_filled_event = threading.Event()
        self.sum_calculated_event = threading.Event()
        self.average_calculated_event = threading.Event()

    def fill_list(self):
        with self.lock:
            self.list = [random.randint(1, 100) for i in range(10)]
            print("Список случайных чисел:", self.list)
            self.list_filled_event.set()

    def calculate_sum(self):
        self.list_filled_event.wait()
        with self.lock:
            result_sum = sum(self.list)
            print("Сумма чисел равна:", result_sum)
            self.sum_calculated_event.set()

    def calculate_average(self):
        self.list_filled_event.wait()
        with self.lock:
            result_average = sum(self.list) / len(self.list)
            print("Среднеарифмеическое значение равно:", result_average)
            self.average_calculated_event.set()


if __name__ == "__main__":
    shared_list = ThreadSafeList()

    fill_thread = threading.Thread(target=shared_list.fill_list)
    sum_thread = threading.Thread(target=shared_list.calculate_sum)
    average_thread = threading.Thread(target=shared_list.calculate_average)

    fill_thread.start()

    sum_thread.start()
    average_thread.start()

    fill_thread.join()

    sum_thread.join()
    average_thread.join()
##########################__ЗАДАНИЕ_2__########################################
import threading
import random
import math


class ThreadSafeFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.lock = threading.Lock()

    def write(self, data):
        with self.lock:
            with open(self.file_path, "a") as file:
                file.write(str(data) + "\n")


def fill_file_with_random_numbers(file_path, total_numbers):
    with open(file_path, "w") as file:
        for _ in range(total_numbers):
            file.write(str(random.randint(1, 100)) + "\n")


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def find_primes_and_write(file_path, result_file):
    with open(file_path, "r") as file:
        for line in file:
            number = int(line.strip())
            if is_prime(number):
                result_file.write(f"Простое число из списка: {number}")


def calculate_factorials_and_write(file_path, result_file):
    with open(file_path, "r") as file:
        for line in file:
            number = int(line.strip())
            result = math.factorial(number)
            result_file.write(f"Факториал числа {number} равен: {result}")


def main():
    file_path = input("Введите путь к файлу: ")
    total_numbers = 10
    result_file_path = "result.txt"
    result_file = ThreadSafeFile(result_file_path)
    fill_thread1 = threading.Thread(
        target=fill_file_with_random_numbers, args=(file_path, total_numbers)
    )
    primes_thread = threading.Thread(
        target=find_primes_and_write, args=(file_path, result_file)
    )
    factorials_thread = threading.Thread(
        target=calculate_factorials_and_write, args=(file_path, result_file)
    )

    fill_thread1.start()
    fill_thread1.join()

    primes_thread.start()
    factorials_thread.start()

    primes_thread.join()
    factorials_thread.join()

    print("Статистика:")
    with open(result_file_path, "r") as result_file:
        for line in result_file:
            print(line.strip())


if __name__ == "__main__":
    main()
##########################__ЗАДАНИЕ_3__########################################
#########################_________НЕ ПОЛУЧАЕТСЯ - ПОСТОЯННО ПИШЕТ ОШИБКУ ПРИ КОПИРОВАНИИ
import threading
import shutil


def copy_files(src, dest, result_list):
    try:
        shutil.copytree(src, dest)
        result_list.append(f"Копирование завершено!")
    except Exception:
        result_list.append(f"Ошибка при копировании!")


def main():
    src_path = input("Введите путь к существующей директории: ")
    dest_path = input("Введите путь к новой директории: ")

    result_list = []

    copy_thread = threading.Thread(
        target=copy_files, args=(src_path, dest_path, result_list)
    )

    copy_thread.start()
    copy_thread.join()

    print("Статистика:")
    for result in result_list:
        print(result)


if __name__ == "__main__":
    main()
##########################__ЗАДАНИЕ_4__########################################
#####################________не сохраняет результат не могу понять почему
import os
import threading


def find_and_merge_files(directory, search_word, result_file):
    with open(result_file, "w") as output_file:
        for root, i, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as input_file:
                        content = input_file.read()
                        if search_word in content:
                            output_file.write(content)
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")


def remove_forbidden_words(input_file, forbidden_words_file, output_file):
    with open(input_file, "r", encoding="utf-8") as input_file:
        content = input_file.read()

        with open(forbidden_words_file, "r", encoding="utf-8") as forbidden_file:
            forbidden_words = forbidden_file.read().split()

        for word in forbidden_words:
            content = content.replace(word, "")

        with open(output_file, "w", encoding="utf-8") as output_file:
            output_file.write(content)


def main():
    directory = input("Введите путь к директории: ")
    search_word = input("Введите слово для поиска: ")

    result_file = "merged_files.txt"
    forbidden_words_file = "zapret.txt"
    output_file = "output.txt"

    thread1 = threading.Thread(
        target=find_and_merge_files, args=(directory, search_word, result_file)
    )
    thread1.start()

    thread1.join()

    thread2 = threading.Thread(
        target=remove_forbidden_words,
        args=(result_file, forbidden_words_file, output_file),
    )
    thread2.start()

    thread2.join()

    print("Операции выполнены успешно.")
    print(f"Результат сохранен в файле {output_file}")


if __name__ == "__main__":
    main()
