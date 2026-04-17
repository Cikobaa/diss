#!/usr/bin/env python3
"""Basit 4 işlemli hesap makinası."""


def to_float(value: str) -> float:
    """Kullanıcıdan gelen değeri float'a çevirir."""
    return float(value.replace(",", "."))


def calculate(a: float, b: float, operation: str) -> float:
    """İstenen matematiksel işlemi uygular."""
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        if b == 0:
            raise ZeroDivisionError("Sıfıra bölme hatası.")
        return a / b
    raise ValueError("Geçersiz işlem. Lütfen +, -, * veya / seçin.")


def main() -> None:
    print("=== Basit Hesap Makinası (4 işlem) ===")
    try:
        first = to_float(input("1. sayı: "))
        operation = input("İşlem (+, -, *, /): ").strip()
        second = to_float(input("2. sayı: "))
        result = calculate(first, second, operation)
        print(f"Sonuç: {result}")
    except ValueError as err:
        print(f"Hata: {err}")
    except ZeroDivisionError as err:
        print(f"Hata: {err}")


if __name__ == "__main__":
    main()
