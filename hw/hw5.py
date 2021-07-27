# *ЗАДАЧА 1:
# Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов: know(person), который позволяет
# добавить другого человека в список знакомых. И метод is_known(person), который возвращает знакомы ли два человека
class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

        self.acquainted = []

    def know(self, person):
        self.acquainted.append(person)

    def is_known(self, person):
        if person in self.acquainted:
            print('You know him/her!')
        else:
            print('You don\'t know him/her')


# p1 = Person(17, 'Sergei')
# p2 = Person(16, 'Andrey')
# p3 = Person(20, 'Vlad')
#
# p1.know(p2)
# p1.is_known(p2)
# p1.is_known(p3)


# *ЗАДАЧА 2:
# Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *

def formattedPrinter(log):
    def wrapper(*values):
        print('***')
        log(*values)
        print('***')

    return wrapper


class Printer:
    # @formattedPrinter
    def log(self, *values):
        print(*values)


class FormattedPrinter(Printer):
    def log(self, *values):
        print('***')
        super().log(*values)
        print('***')


# p1 = Printer()
# p1.log('Hello')
# p2 = FormattedPrinter()
# p2.log('Hello')

# *ЗАДАЧА 3:
# Написать класс Animal и Human,сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)

class Animal:
    def __init__(self, name, dangerous):
        self.name = name
        self.dangerous = dangerous


class Human:
    def is_dangerous(self, animal: Animal):
        if animal.dangerous:
            print(f'{animal.name} is dangerous! Run!')
        else:
            print(f'{animal.name} is not dangerous. You can free breath)')


# a1 = Animal('Lion', True)
# a2 = Animal('Cat', False)
#
# h1 = Human()
# h1.is_dangerous(a1)
# h1.is_dangerous(a2)

