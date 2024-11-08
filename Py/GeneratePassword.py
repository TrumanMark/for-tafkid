import random
import string
import os
import tkinter as tk
from tkinter import ttk

# Настройка символов пароля
def password_complete(include_letters, include_numbers, include_special_chars):
    char = ""
    if include_letters:
        char += string.ascii_letters
    if include_numbers:
        char += string.digits
    if include_special_chars:
        char += string.punctuation
    return char

# Генерация пароля
def generate_password(size, char):
    password = ''.join(random.choice(char) for _ in range(size))
    return password

# Сохранение пароля в файл
def save_password_to_file(name, password):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "generated_passwords.txt")
    
    # Проверяем, существует ли файл
    file_exists = os.path.exists(desktop_path) and os.path.getsize(desktop_path) > 0
    with open(desktop_path, "a") as file:
        if file_exists:
            file.write("\n\n")  # Добавляем пустую строку между старыми и новыми записями
        file.write(f"Name: {name}\n")
        file.write(f"Password: {password}\n")
    
    print(f"Data saved on the desktop in 'generated_passwords.txt'")

# Основные настройки для терминального режима работы
def basic_settings():
    name = input('Enter your name: ')
    size = int(input('Enter password size: '))
    print("Setup password complexity, for each option enter yes or no:")
    include_letters = input('Include all letters of the alphabet? (yes/no): ') == 'yes'
    include_numbers = input('Include numbers? (yes/no): ') == 'yes'
    include_special_chars = input('Include special characters? (yes/no): ') == 'yes'
    return name, include_letters, include_numbers, include_special_chars, size

# Генерация и вывод пароля в терминал
def terminal_mode():
    name, include_letters, include_numbers, include_special_chars, size = basic_settings()
    char = password_complete(include_letters, include_numbers, include_special_chars)
    password = generate_password(size, char)
    print(f"Name: {name}\nPassword: {password}")

# Генерация и сохранение пароля в файл
def file_mode():
    name, include_letters, include_numbers, include_special_chars, size = basic_settings()
    char = password_complete(include_letters, include_numbers, include_special_chars)
    password = generate_password(size, char)
    save_password_to_file(name, password)

# Функция для обработки кнопки "Generate Password"
def generate_and_save():
    name = entry_name.get()
    size = int(entry_size.get())
    include_letters = var_letters.get()
    include_numbers = var_numbers.get()
    include_special_chars = var_special_chars.get()

    # Генерация пароля
    char = password_complete(include_letters, include_numbers, include_special_chars)
    password = generate_password(size, char)
    
    # Отображаем сгенерированный пароль
    label_result.config(text=f"Generated Password: {password}")
    
    # Если флажок установлен, сохраняем в файл
    if var_save_to_file.get():
        save_password_to_file(name, password)

# Графический интерфейс для режима 3
def graphical_interface_mode():
    # Создаем главное окно для графического интерфейса
    root = tk.Tk()
    root.title("Password Generator")

    # Настроим стиль с использованием ttk
    style = ttk.Style()
    style.configure("TButton", padding=6, relief="flat", background="#ccc")
    style.configure("TLabel", padding=6)

    # Ввод имени
    label_name = ttk.Label(root, text="Enter your name:")
    label_name.pack(pady=5)
    global entry_name
    entry_name = ttk.Entry(root, width=40)
    entry_name.pack(pady=5)

    # Ввод размера пароля
    label_size = ttk.Label(root, text="Enter password size:")
    label_size.pack(pady=5)
    global entry_size
    entry_size = ttk.Entry(root, width=40)
    entry_size.pack(pady=5)

    # Опции для выбора сложности пароля
    global var_letters, var_numbers, var_special_chars, var_save_to_file
    var_letters = tk.BooleanVar()
    check_letters = ttk.Checkbutton(root, text="Include letters (a-z, A-Z)", variable=var_letters)
    check_letters.pack(pady=5)

    var_numbers = tk.BooleanVar()
    check_numbers = ttk.Checkbutton(root, text="Include numbers (0-9)", variable=var_numbers)
    check_numbers.pack(pady=5)

    var_special_chars = tk.BooleanVar()
    check_special_chars = ttk.Checkbutton(root, text="Include special characters (!@#$%^&*)", variable=var_special_chars)
    check_special_chars.pack(pady=5)

    # Флажок для выбора, сохранять ли в файл
    var_save_to_file = tk.BooleanVar()
    check_save_to_file = ttk.Checkbutton(root, text="Save to file?", variable=var_save_to_file)
    check_save_to_file.pack(pady=5)

    # Кнопка для генерации пароля
    button_generate = ttk.Button(root, text="Generate Password", command=generate_and_save)
    button_generate.pack(pady=10)

    # Место для отображения сгенерированного пароля
    global label_result
    label_result = ttk.Label(root, text="Generated Password: ", font=("Arial", 12))
    label_result.pack(pady=5)

    # Запускаем главный цикл интерфейса
    root.mainloop()

# Основная логика выбора режима работы программы
def choose_program_mode():
    type_program = int(input("Select the program's operating mode:\n1 - Interaction mode: terminal, displaying name and password in the terminal \n2 - Interaction mode: terminal, output: create a txt file on the desktop \n3 - Interaction mode: graphical interface \nyour choice: "))
    
    if type_program == 1:
        terminal_mode()
    
    elif type_program == 2:
        file_mode()
    
    elif type_program == 3:
        graphical_interface_mode()

# Запуск выбора режима
choose_program_mode()
