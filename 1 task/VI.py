try:
    cat_name = int("Whiskers")
except ValueError:
    print("О, ні! Ваша кішка не є числом!")
    print("Спробуйте дати їй ім'я, яке складається лише з цифр.")
except Exception as e:
    print(f"Щось пішло не так: {e}")
finally:
    print("Нам дуже шкода, що не вийшло. Спробуйте ще раз з іншою кішкою! 😸")