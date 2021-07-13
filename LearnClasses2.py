import time


class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    # def __del__(self):
    #     print(self.name, 'удален из памяти')

    def display_info(self):
        print('Привет, меня зовут', self.__name + '. Мой возраст:', self.__age, 'лет.')

    # def set_age(self, age):
    #     if 0 <= age <= 70:
    #         self.__age = age
    #     else:
    #         print('Wrong age!')
    #
    # def set_name(self, name):
    #     self.__name = name

    @property
    def age(self, age):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print('Wrong age!!!')

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.__name = name



person1 = Person('Tom')
person1.display_info()
person1.age = 5
person1.name = 'Paul'
person1.display_info()

