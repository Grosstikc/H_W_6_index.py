from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        self.validate_phone(value)
        super().__init__(value)

    def validate_phone(self, value):
        if not re.match(r'^\d{10}$', value):
            raise ValueError("Invalid phone number format. It should have 10 digits.")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError(f"Phone number '{old_phone}' not found.")

    def find_phone(self, number):
        found_phones = [phone for phone in self.phones if phone.value == number]
        if not found_phones:
            return None
        return found_phones[0]  # Повертаємо перший знайдений об'єкт класу Phone


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


# Створення нової адресної книги
book = AddressBook()

# Створення запису для Mary
mary_record = Record("Mary")
mary_record.add_phone("1112223333")

# Додавання запису Mary до адресної книги
book.add_record(mary_record)

# Створення та додавання нового запису для Bob
bob_record = Record("Bob")
bob_record.add_phone("4445556666")
bob_record.add_phone("7778889999")
book.add_record(bob_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для Bob
bob = book.find("Bob")
bob.edit_phone("4445556666", "0009998888")

print(bob)  # Виведення: Contact name: Bob, phones: 0009998888; 7778889999

# Пошук конкретного телефону у записі Bob
try:
    found_phone = bob.find_phone("7778889999")
    print(f"{bob.name}: {found_phone}")  # Виведення: 7778889999
except ValueError as e:
    print(e)

# Видалення запису Mary
book.delete("Mary")
