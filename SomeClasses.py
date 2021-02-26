# Task 8
class Rectangle:
    def __init__(self, initb, inith):
        self.b = initb
        self.h = inith
    def area(self):
        return self.b * self.h

from math import pi
class Circle:
    def __init__(self, initr):
        self.r = initr
    def area(self):
        return self.r * self.r * pi


# Task 9
class Product:
    def __init__(self, initn, initp):
        self.name = initn
        self.price = initp
    def __str__(self):
        return self.name + " costs " + str(self.price) + " euro(s)"

# Task 10
class PhoneBook:
    def __init__(self):
        self.names = []
        self.numbers = []

    def add_number(self, name, number):
        """
       Add a contact or throw InvalidOperationException if it is already present
        :param number: an integer number
        :param name: a string
       """
        if name not in self.names:
            pos = next((i for i, record in enumerate(self.names) if name < record ), -1)
            if pos == -1:
                self.names.append(name)
                self.numbers.append(number)
            else:
                self.names.insert(pos, name)
                self.numbers.insert(pos, number)
        else:
            pass

    def del_number(self, name):
        """
        Delete a contact or throw InvalidOperationException if it is not present
        :param name: a string
        """
        if name in self.names:
            pos = self.names.index(name)
            self.names.pop(pos)
            self.numbers.pop(pos)
        else:
            pass

    def size(self):
        """
        :return: current size of PhoneBook
        """
        return len(self.names)

    def get_all(self):
        """
        return: a string representation of all entries in the format 'name: number',
        merged and separated by ';' and a space. The entries should be sorted alphabetically
        """
        output = ""
        for i in range(len(self.names)):
            output += self.names[i] + ": " + str(self.numbers[i])
            if i != len(self.names) - 1:
                output += "; "
        return output
