# читаем адресную книгу в формате CSV в список contacts_list
import csv

# import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# функция помещает Фамилию, Имя и Отчество человека в поля lastname, firstname и surname,
# вернет измененный contact list
def name_assembly():
    names_sorted = contacts_list[1:]  # пропускаю заголовок
    processed_list = []  # временный список с без заголовка
    for i in names_sorted:
        new_list = i.copy()
        name_list = " ".join(i[:3]).split(" ")[:3]
        new_list[:3] = name_list
        processed_list.append(new_list)
    contacts_list[1:] = processed_list


# функция объединяет дубли
def de_duplicates():
    pass


# функция приводит номера телефонов к единому формату: +7(999)999-99-99 доб.9999
def reformat_phone_numbers():
    pass

# # код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
