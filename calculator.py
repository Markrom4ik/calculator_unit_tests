def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Нельзя делить на ноль")
    return a / b


def main():
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /")

    a = float(input("Введите первое число: "))
    operation = input("Введите операцию: ")
    b = float(input("Введите второе число: "))

    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    else:
        print("Неизвестная операция")
        return

    print("Результат:", result)


if __name__ == "__main__":
    main()
