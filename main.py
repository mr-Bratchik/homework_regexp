# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# функция помещает Фамилию, Имя и Отчество человека в поля lastname, firstname и surname,
# вернет измененный contact list
def name_assembly(input_contacts):
    processed_list = []  # временный список без заголовка
    for i in input_contacts[1:]:  # пропускаю заголовок
        new_list = i.copy()
        name_list = " ".join(i[:3]).split(" ")[:3]
        new_list[:3] = name_list
        processed_list.append(new_list)
    input_contacts[1:] = processed_list
    return input_contacts


# функция объединяет дубли
def de_duplicates(input_contacts):
    processed_dict = {}  # Словарь для хранения уникальных контактов
    for contact in input_contacts[1:]:
        key = (contact[0], contact[1])  # Ключ для проверки уникальности (Фамилия, Имя)
        if key in processed_dict:
            new_values = []
            for i, val in enumerate(processed_dict[key]):
                if val:
                    new_values.append(val)
                else:
                    new_values.append(contact[i])
            processed_dict[key] = new_values
        else:
            processed_dict[key] = contact

    # Собираем новый список контактов
    deduplicated_list = [input_contacts[0]]
    for values in processed_dict.values():
        deduplicated_list.append(values)

    return deduplicated_list


# функция приводит номера телефонов к единому формату: +7(999)999-99-99 доб.9999
def normalize_phone(phone):
    pattern = r"(\+7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(?:\s*\(?(доб\.?)\s*(\d+)\)?)?"
    substitution = r"+7(\2)\3-\4-\5"
    match = re.search(pattern, phone)
    if match:
        base_phone = re.sub(pattern, substitution, phone)
        ext = match.group(7)  # Извлекаем добавочный номер
        return f"{base_phone} доб.{ext}" if ext else base_phone
    return phone



# функция нормализует телефоны в списке контактов
def normalize_phone_in_contacts(input_contacts):
    for contact in input_contacts[1:]:  # Пропускаем заголовок
        contact[5] = normalize_phone(contact[5])  # Нормализуем телефонный номер в 6-м поле
    return input_contacts


# Применяем функции
contacts_list = name_assembly(contacts_list)
contacts_list = de_duplicates(contacts_list)
contacts_list = normalize_phone_in_contacts(contacts_list)

# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)
