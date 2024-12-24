def hex_to_ascii_utf8(hex_value):
    try:
        # Преобразование в ASCII
        ascii_value = bytes.fromhex(hex_value).decode('ascii')
    except (ValueError, UnicodeDecodeError):
        ascii_value = "[Невозможно преобразовать в ASCII]"

    try:
        # Преобразование в UTF-8
        utf8_value = bytes.fromhex(hex_value).decode('utf-8')
    except (ValueError, UnicodeDecodeError):
        utf8_value = "[Невозможно преобразовать в UTF-8]"

    return ascii_value, utf8_value

def perform_operations(hex1, hex2):
    try:
        # Преобразование из шестнадцатеричного в десятичное
        dec1 = int(hex1, 16)
        dec2 = int(hex2, 16)

        # Арифметические операции
        sum_result = dec1 + dec2
        sub_result = dec1 - dec2
        mul_result = dec1 * dec2
        div_result = dec1 // dec2 if dec2 != 0 else None

        # Преобразование результатов обратно в шестнадцатеричное
        results = {
            'Сложение': hex(sum_result)[2:],
            'Вычитание': hex(sub_result)[2:] if sub_result >= 0 else f'-{hex(abs(sub_result))[2:]}',
            'Умножение': hex(mul_result)[2:],
            'Деление': hex(div_result)[2:] if div_result is not None else '[Деление на 0]'
        }

        return results

    except ValueError:
        return "[Ошибка: Некорректный ввод шестнадцатеричных данных]"

# Основная программа
if __name__ == "__main__":
    print("Введите два шестнадцатеричных числа (без префикса 0x):")
    hex1 = input("Первое число: ").strip()
    hex2 = input("Второе число: ").strip()

    results = perform_operations(hex1, hex2)

    if isinstance(results, str):
        print(results)
    else:
        for operation, result in results.items():
            ascii_value, utf8_value = hex_to_ascii_utf8(result)
            print(f"\n{operation}:")
            print(f"Шестнадцатеричный: {result}")
            print(f"ASCII: {ascii_value}")
            print(f"UTF-8: {utf8_value}")
