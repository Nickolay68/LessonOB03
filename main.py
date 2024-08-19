# Создаем базовый класс Animal, который будет содержать общие атрибуты
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен подклассами")

    def eat(self):
        return f"{self.name} is eating."

# Создаем подклассы, которые наследуют от Animal.
# Каждый из этих классов будет иметь специфические атрибуты и переопределенный метод make_sound().
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return f"{self.name} щебечет."

    def fly(self):
        return f"{self.name} летит с размахом крыльев в {self.wing_span} метров."

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return f"{self.name} рычит."

    def run(self):
        return f"{self.name} бежит."

class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        return f"{self.name} шипит."

    def crawl(self):
        return f"{self.name} ползет."

# Создаем функцию animal_sound, которая принимает список животных
# и вызывает метод make_sound() для каждого из них.
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

# Создаем класс Zoo, который будет содержать списки животных и сотрудников.
# В нем будут методы для добавления новых животных и сотрудников.
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Added {staff_member.name} для персонала.")

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name} ({animal.__class__.__name__}), лет: {animal.age}")

    def show_staff(self):
        for staff in self.staff:
            print(f"{staff.name} ({staff.__class__.__name__})")

# Создаем классы сотрудников с их специфическими методами, такими как кормление животных и лечение.
class Staff:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Staff):
    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}."

class Veterinarian(Staff):
    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}."

# Теперь создаем объекты животных, сотрудников и зоопарка, а также демонстрируем работу функций и классов.

eagle = Bird(name="Орёл", age=5, wing_span=2.5)
lion = Mammal(name="Лев", age=8, fur_color="Золотой")
snake = Reptile(name="Змея", age=3, scale_color="Зелёная")

# Создаем объект зоопарка
zoo = Zoo()

# Добавляем животных в зоопарк
zoo.add_animal(eagle)  # Используем переменную eagle
zoo.add_animal(lion)   # Используем переменную lion
zoo.add_animal(snake)  # Используем переменную snake

# Создаем объекты сотрудников
zookeeper = ZooKeeper(name="Ваня")
vet = Veterinarian(name="Доктор")

# Добавляем сотрудников в зоопарк
zoo.add_staff(zookeeper)
zoo.add_staff(vet)

# Показать всех животных в зоопарке
zoo.show_animals()

# Показать всех сотрудников зоопарка
zoo.show_staff()

# Полиморфизм
animals = [eagle, lion, snake]  # Используем правильные переменные
animal_sound(animals)

# Работа сотрудников
print(zookeeper.feed_animal(lion))
print(vet.heal_animal(snake))
