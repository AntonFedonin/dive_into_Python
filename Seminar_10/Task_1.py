# Доработаем задачи 5-6. Создайте класс-фабрику.
#     ○ Класс принимает тип животного (название одного из созданных классов)
#        и параметры для этого типа.
#     ○ Внутри класса создайте экземпляр на основе
#       переданного типа и верните его из класса-фабрики.


class Animal:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        pass


class Bird(Animal):
    def __init__(self, name, wing_size):
        super().__init__(name)
        self.wing_size = wing_size

    def get_info(self):
        return f'Размах крыла у {self.name} = {self.wing_size} см'


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def get_info(self):
        return f'Порода собаки {self.name} = {self.breed}'


class Cow(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def get_info(self):
        return f'Вес коровы {self.name} = {self.weight} кг'


class RedBook(Animal):
    def __init__(self, name, count):
        super().__init__(name)
        self.count = count

    def get_info(self):
        return f' {self.name} на земле осталось {self.count}'


class AnimalFactory:
    def __init__(self):
        self.animals = {
            'Bird': Bird,
            'Dog': Dog,
            'Cow': Cow,
            'RedBook': RedBook
        }

    def create_card(self, animals, *args):
        animals = self.animals[animals]
        return animals(*args)


if __name__ == "__main__":
    factory = AnimalFactory()
    bird = factory.create_card('Bird', 'Snowy owl', 67)
    dog = factory.create_card('Dog', 'Мухтар', 'Овчарка')
    cow = factory.create_card('Cow', 'Бурёнка', 720)
    red_book = factory.create_card('RedBook', 'Amur tiger', 600)

    print(bird.get_info())
    print(dog.get_info())
    print(cow.get_info())
    print(red_book.get_info())