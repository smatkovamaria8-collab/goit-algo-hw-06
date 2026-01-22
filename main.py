from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class WrongSizeNumberError(Exception):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if len(self.value) != 10 or not self.value.isdigit():
            raise WrongSizeNumberError("Please enter a valid phone number size - 10")



class NotFoundNumber(ValueError):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        try:
            self.phones.remove(self.find_phone(phone))
        except ValueError:
            raise NotFoundNumber('This phone number: {phone} is not present in the record')

    def edit_phone(self, old_phone, new_phone):
        try:
            number = self.phones.index(self.find_phone(old_phone))
            self.phones[number] = Phone(new_phone)
        except ValueError:
            raise NotFoundNumber('This phone number: {phone} is not present in the record')

    def find_phone(self, phone):
        for phone_contact in self.phones:
            if phone_contact.value == phone:
                return phone_contact
        else:
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        contact = self.data.get(name)
        return contact

    def delete(self, name):
        try:
            del self.data[name]
        except KeyError:
            return f'Such record of {name} was not found'

    def __str__(self):
        list_contact = []
        for key in self.data:
            list_contact.append(self.data[key])
        return f' {'\n'.join(str(p) for p in list_contact)}'


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")


# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
print(book)
