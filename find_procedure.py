
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

# import glob
# migrations = 'Migrations'
# files = glob.glob(os.path.join(migrations, "*.sql"))
# print(files)


import os
dir_list = []
for root, dirs, files in os.walk("Migrations", topdown=False):
	for name in files:
		dir = os.path.join(root, name)
		dir_list.append(dir)
sql_list = []

for line in dir_list:
	if ".sql" in line:
		sql_list.append(line)

first_variable_list = []
def first_search(var):
	for line in sql_list:
		if var.lower() in line:
			first_variable_list.append(line)
	for line in first_variable_list:
		print(line)
	print(len(first_variable_list), "files have been found.")

second_variable_list = []
def second_search(var):
	for line in first_variable_list:
		if var.lower() in line:
			second_variable_list.append(line)
	for line in second_variable_list:
		print(line)
	print(len(second_variable_list), "files have been found")

third_variable_list = []
def third_search(var):
	for line in second_variable_list:
		if var.lower() in line:
			third_variable_list.append(line)
	for line in third_variable_list:
		print(line)
	print(len(third_variable_list), "files have been found")


first_enter = input("Search: ")
first_search(first_enter)
second_enter = input("Second search: ")
second_search(second_enter)
third_enter = input("Third search: ")
third_search(third_enter)
