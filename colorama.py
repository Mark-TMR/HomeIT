

# Імпорт бібліотеки
import colorama

# Перегляд усіх атрибутів і методів бібліотеки
print("=== Інтроспекція бібліотеки colorama ===")
print(dir(colorama))  # показує усі доступні елементи модуля

# 3. Найважливіші атрибути та методи:
# colorama.init() – ініціалізує бібліотеку (особливо потрібно в Windows)
# colorama.deinit() – вимикає кольори та повертає консоль у стандартний стан
# colorama.Fore – набір кольорів тексту (наприклад: Fore.RED, Fore.BLUE)
# colorama.Back – набір кольорів фону (наприклад: Back.GREEN, Back.MAGENTA)
# colorama.Style – стилі відображення тексту (BRIGHT, DIM, RESET_ALL)
# colorama.Cursor – дозволяє керувати положенням курсора
# colorama.just_fix_windows_console() – автоматично виправляє кольори у Windows

#Приклад використання colorama
from colorama import Fore, Back, Style, init

# Показання бібліотеки
init()

print(Fore.RED + 'Це червоний текст')
print(Back.GREEN + 'А це текст на зеленому фоні')
print(Style.BRIGHT + 'Яскравий стиль тексту')
print(Style.RESET_ALL + 'Повернення до стандартного стилю')

# Пояснення:
# Fore — задає колір переднього плану (тексту)
# Back — задає колір фону
# Style — додає яскравість або скидає всі стилі
# RESET_ALL — повертає кольори до стандартних
# init() — активує кольоровий режим
# deinit() — завершує роботу бібліотеки

#Завершення роботи
colorama.deinit()
