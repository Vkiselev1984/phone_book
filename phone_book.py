from csv import DictReader, DictWriter
from os.path import exists
from tabulate import tabulate

phone_data = 'phone_data.csv'
copy_phone_data = 'copy_phone_data.csv'

def get_info():
    record = {}
    record['Имя'] = input('Введите имя: ')
    record['Фамилия'] = input('Введите фамилию: ')
    
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print("Неверная длина номера")
            else:
                record['Телефон'] = phone_number
                flag = True
        except ValueError:
            print("Не валидный номер")
    return record

def create_file(phone_data):
    with open(phone_data, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        
def read_file(phone_data):
    with open(phone_data, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)

def write_file(phone_data, record):
    data = read_file(phone_data)
    if not data:
        record['ID'] = 1
    else:
        last_id = int(data[-1]['ID'])
        record['ID'] = last_id + 1
    data.append(record)
    with open(phone_data, 'w', encoding='utf-8', newline='') as file:
        fieldnames = ['ID', 'Имя', 'Фамилия', 'Телефон']
        writer = DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def copy_record(phone_data, copy_phone_data, record_num=None):
    source_data = read_file(phone_data)
    dest_data = read_file(copy_phone_data)
    
    if record_num is None:
        for record in source_data:
            if record not in dest_data:
                dest_data.append(record)
    else:
        if record_num <= 0 or record_num > len(source_data):
            print('Некорректный номер записи')
            return
        record_to_copy = source_data[record_num - 1]
        match_found = False
        for dest_record in dest_data:
            if all(record_to_copy[key] == dest_record[key] for key in ['Имя', 'Фамилия', 'Телефон']):
                match_found = True
                break
        if not match_found:
            dest_data.append(record_to_copy)
        else:
            print('Запись уже существует в целевом файле')
    with open(copy_phone_data, 'w', encoding='utf-8', newline='') as file:
        fieldnames = ['ID', 'Имя', 'Фамилия', 'Телефон']
        writer = DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dest_data)

def print_table(data):
    headers = ['ID', 'Имя', 'Фамилия', 'Телефон']
    table = [[record['ID'], record['Имя'], record['Фамилия'], record['Телефон']] for record in data]
    print(tabulate(table, headers=headers, tablefmt='grid'))
    
def delete_record(phone_data, record_num):
    data = read_file(phone_data)
    
    if record_num <= 0 or record_num > len(data):
        print('Некорректный номер записи')
        return
    
    del_record = data.pop(record_num - 1)
    
    for index, record in enumerate(data):
        record['ID'] = index + 1
    
    with open(phone_data, 'w', encoding='utf-8', newline='') as file:
        fieldnames = ['ID', 'Имя', 'Фамилия', 'Телефон']
        writer = DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f'Запись с ID {del_record["ID"]} удалена')

def clear_copy_table(copy_phone_data):
    with open(copy_phone_data, 'w', encoding='utf-8', newline='') as file:
        fieldnames = ['ID', 'Имя', 'Фамилия', 'Телефон']
        writer = DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

def Main():
    while True:
        command = input('Введите команду (add_person, show_table, show_copy_table, copy_person, copy_table, delete_person, clear_copy_table, info, exit): ')
        if command == 'exit':
            break
        elif command == 'add_person':
            if not exists(phone_data): 
                create_file(phone_data)
            record = get_info()  
            if record: 
                write_file(phone_data, record)
                print('Запись добавлена')
            else:
                print('Ошибка валидации. Повторите ввод.')
        elif command == 'show_table':
            if not exists(phone_data):
                print('Файл отсутствует. Создайте его')
                continue
            data = read_file(phone_data)
            print_table(data)
        elif command == 'copy_person':
            if not exists(phone_data):
                print('Файл отсутствует. Создайте его')
                continue
            record_num = int(input('Введите номер строки для копирования: '))
            copy_record(phone_data, copy_phone_data, record_num)
        elif command == 'copy_table':
            if not exists(phone_data):
                print('Файл отсутствует. Создайте его')
                continue
            copy_record(phone_data, copy_phone_data)
            print('Справочник скопирован полностью')
        elif command == 'delete_person':
            if not exists(phone_data):
                print('Файл отсутствует. Создайте его')
                continue
            record_num = int(input('Введите номер строки для удаления: '))
            delete_record(phone_data, record_num)
            print('Запись удалена')
        elif command == 'info':
            print('Добавить запись в справочник: add_person')
            print('Прочитать записи: show_table')
            print('Скопировать запись: copy_person')
            print('Скопировать весь справочник: copy_table')
            print('Удалить запись: delete_person')
            print('Очистить вторую таблицу: clear_copy_table')
            print('Выйти: exit')
        elif command == 'show_copy_table':
            if not exists(copy_phone_data):
                print('Файл со скопированными данными отсутствует')
                continue
            copy_data = read_file(copy_phone_data)
            print_table(copy_data)
        elif command == 'clear_copy_table':
            if not exists(copy_phone_data):
                print('Файл со скопированными данными отсутствует')
                continue
            clear_copy_table(copy_phone_data)
            print('Вторая таблица очищена')
        else:
            print('Некорректная команда. Повторите ввод.')

Main()