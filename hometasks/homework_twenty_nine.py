##############################____ЗАДАНИЕ 1_______########################################
def main():
    numbers = []

    while True:
        print("\nМеню:")
        print("1. Добавить новое число в список")
        print("2. Удалить все вхождения числа из списка")
        print("3. Показать содержимое списка")
        print("4. Проверить есть ли значение в списке")
        print("5. Заменить значение в списке")
        print("6. Выйти из программы")

        choice = input("Выберите пункт меню (1-6): ")

        if choice == "1":
            number = int(input("Введите число для добавления: "))
            if number not in numbers:
                numbers.append(number)
                print("Число добавлено в список.")
            else:
                print("Число уже существует в списке.")

        elif choice == "2":
            number_to_remove = int(input("Введите число для удаления: "))
            numbers = [x for x in numbers if x != number_to_remove]
            print("Все вхождения числа удалены из списка.")

        elif choice == "3":
            order = input("Выберите порядок вывода (1 - с начала, 2 - с конца): ")
            if order == "1":
                print("Содержимое списка:", numbers)
            elif order == "2":
                print("Содержимое списка (в обратном порядке):", numbers[::-1])
            else:
                print("Неверный выбор порядка.")

        elif choice == "4":
            value_to_check = int(input("Введите значение для проверки: "))
            if value_to_check in numbers:
                print("Значение найдено в списке.")
            else:
                print("Значение не найдено в списке.")

        elif choice == "5":
            value_to_replace = int(input("Введите значение для замены: "))
            new_value = int(input("Введите новое значение: "))
            replace_all = input("Заменить все вхождения? (y/n): ").lower() == "y"

            if replace_all:
                numbers = [new_value if x == value_to_replace else x for x in numbers]
            else:
                if value_to_replace in numbers:
                    index = numbers.index(value_to_replace)
                    numbers[index] = new_value
                    print("Значение заменено.")
                else:
                    print("Значение не найдено в списке.")

        elif choice == "6":
            print("Программа завершена.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 6.")


if __name__ == "__main__":
    main()


##############################____ЗАДАНИЕ 2_______########################################
class FixedSizeStack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, value):
        if self.is_full():
            print("Стек полон. Невозможно добавить значение.")
        else:
            self.top += 1
            self.stack[self.top] = value
            print(f"Добавлено значение: {value}")

    def pop(self):
        if self.is_empty():
            print("Стек пуст. Невозможно извлечь значение.")
            return None
        else:
            value = self.stack[self.top]
            self.top -= 1
            print(f"Извлечено значение: {value}")
            return value

    def peek(self):
        if self.is_empty():
            print("Стек пуст.")
            return None
        else:
            value = self.stack[self.top]
            print(f"Верхнее значение в стеке: {value}")
            return value

    def count(self):
        return self.top + 1

    def clear(self):
        self.stack = [None] * self.size
        self.top = -1
        print("Стек очищен.")


size = int(input("Введите размер стека: "))
stack = FixedSizeStack(size)

while True:
    print("Меню:")
    print("1 - Поместить значение в стек")
    print("2 - Вытолкнуть значение из стека")
    print("3 - Подсчет количества значений в стеке")
    print("4 - Проверить, пуст ли стек")
    print("5 - Проверить, полон ли стек")
    print("6 - Очистить стек")
    print("7 - Получить значение без выталкивания")
    print("8 - Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        value = int(input("Введите целое значение для добавления в стек: "))
        stack.push(value)
    elif choice == "2":
        stack.pop()
    elif choice == "3":
        count = stack.count()
        print(f"Количество значений в стеке: {count}")
    elif choice == "4":
        if stack.is_empty():
            print("Стек пуст.")
        else:
            print("Стек не пуст.")
    elif choice == "5":
        if stack.is_full():
            print("Стек полон.")
        else:
            print("Стек не полон.")
    elif choice == "6":
        stack.clear()
    elif choice == "7":
        stack.peek()
    elif choice == "8":
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")

##############################____ЗАДАНИЕ 3_______########################################


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)
        print(f"Добавлено значение: {value}")

    def pop(self):
        if self.is_empty():
            print("Стек пуст. Невозможно извлечь значение.")
            return None
        value = self.stack.pop()
        print(f"Извлечено значение: {value}")
        return value

    def peek(self):
        if self.is_empty():
            print("Стек пуст.")
            return None
        value = self.stack[-1]
        print(f"Верхнее значение в стеке: {value}")
        return value

    def count(self):
        return len(self.stack)

    def clear(self):
        self.stack = []
        print("Стек очищен.")


stack = Stack()

while True:
    print("Меню:")
    print("1. Поместить значение в стек")
    print("2. Вытолкнуть значение из стека")
    print("3. Подсчет количества значений в стеке")
    print("4. Проверить, пуст ли стек")
    print("5. Очистить стек")
    print("6. Получить значение без выталкивания")
    print("7. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        value = int(input("Введите целое значение для добавления в стек: "))
        stack.push(value)
    elif choice == "2":
        stack.pop()
    elif choice == "3":
        count = stack.count()
        print(f"Количество значений в стеке: {count}")
    elif choice == "4":
        if stack.is_empty():
            print("Стек пуст.")
        else:
            print("Стек не пуст.")
    elif choice == "5":
        stack.clear()
    elif choice == "6":
        stack.peek()
    elif choice == "7":
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
