from datetime import datetime, timedelta

class Field:
    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

class Phone(Field):
    def validate_phone(self):
        # Додамо просту перевірку на коректність номера телефону
        if not isinstance(self.value, str) or not self.value.isdigit():
            raise ValueError("Phone number must contain only digits.")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        self.validate_phone()

class Birthday(Field):
    def validate_birthday(self):
        # Додамо просту перевірку на коректність дня народження
        if not isinstance(self.value, datetime):
            raise ValueError("Birthday must be a datetime object.")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        self.validate_birthday()

class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = Field(name)
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday.value:
            today = datetime.now()
            next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day)
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day)
            days_left = (next_birthday - today).days
            return days_left
        return None

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def iterator(self, N):
        for i in range(0, len(self.records), N):
            yield self.records[i:i + N]
