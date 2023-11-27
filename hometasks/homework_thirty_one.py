#############################__ЗАДАНИЕ 1__##################################
class Computer:
    def _init_(self):
        self.components = {}

    def add_component(self, key, value):
        self.components[key] = value

    def _str_(self):
        return f"Компьютер с компонентами: {self.components}"


class ComputerBuilder:
    def _init_(self):
        self.computer = Computer()

    def configure_processor(self, processor):
        self.computer.add_component("процессор", processor)
        return self

    def configure_ram(self, ram):
        self.computer.add_component("оперативная_память", ram)
        return self

    def configure_graphics_card(self, graphics_card):
        self.computer.add_component("графическая_карта", graphics_card)
        return self

    def configure_motherboard(self, motherboard):
        self.computer.add_component("материнкая_плата", motherboard)
        return self

    def configure_power_unit(self, power_unit):
        self.computer.add_component("Блок_питания", power_unit)
        return self

    def configure_SSD_HDD(self, SSD_HDD):
        self.computer.add_component("Накопитель", SSD_HDD)
        return self

    def configure_CPU_cooler(self, CPU_cooler):
        self.computer.add_component("уллер_процессора", CPU_cooler)
        return self

    def configure_frame(self, frame):
        self.computer.add_component("Корпус", frame)
        return self

    def build(self):
        return self.computer


builder = ComputerBuilder()
computer = (
    builder.configure_processor("Intel Core i7")
    .configure_ram("16GB")
    .configure_graphics_card("NVIDIA GTX 3080")
    .configure_motherboard("GIGABYTE")
    .configure_power_unit("VX PLUS 700W")
    .configure_SSD_HDD("Kingsto A400 480 ГБ")
    .configure_CPU_cooler("DEEPCOOL AK620")
    .configure_frame("Cougar Duoface RGB")
    .build()
)
print(computer)
#############################__ЗАДАНИЕ 2__##################################
from abc import ABC, abstractmethod


class Pasta(ABC):
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sauce(self):
        pass

    @abstractmethod
    def get_filling(self):
        pass

    @abstractmethod
    def get_additives(self):
        pass


class SpaghettiPasta(Pasta):
    def get_type(self):
        return "Spaghetti"

    def get_sauce(self):
        return "Tomato Sauce"

    def get_filling(self):
        return "No Filling"

    def get_additives(self):
        return ["Salt", "Olive Oil"]


class PennePasta(Pasta):
    def get_type(self):
        return "Penne"

    def get_sauce(self):
        return "Alfredo Sauce"

    def get_filling(self):
        return "Chicken"

    def get_additives(self):
        return ["Parmesan Cheese", "Black Pepper"]


class FettuccinePasta(Pasta):
    def get_type(self):
        return "Fettuccine"

    def get_sauce(self):
        return "Creamy Mushroom Sauce"

    def get_filling(self):
        return "Mushrooms"

    def get_additives(self):
        return ["Garlic", "Parsley"]


class PastaFactory(ABC):
    @abstractmethod
    def create_pasta(self):
        pass


class SpaghettiFactory(PastaFactory):
    def create_pasta(self):
        return SpaghettiPasta()


class PenneFactory(PastaFactory):
    def create_pasta(self):
        return PennePasta()


class FettuccineFactory(PastaFactory):
    def create_pasta(self):
        return FettuccinePasta()


def make_pasta(factory):
    pasta = factory.create_pasta()
    print(f"Type: {pasta.get_type()}")
    print(f"Sauce: {pasta.get_sauce()}")
    print(f"Filling: {pasta.get_filling()}")
    print(f"Additives: {', '.join(pasta.get_additives())}")
    print()


spaghetti_factory = SpaghettiFactory()
penne_factory = PenneFactory()
fettuccine_factory = FettuccineFactory()

make_pasta(spaghetti_factory)
make_pasta(penne_factory)
make_pasta(fettuccine_factory)

#############################__ЗАДАНИЕ 3__##################################

import copy


class Car:
    def _init_(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def _str_(self):
        return f"{self.color} {self.brand} {self.model}"


if __name__ == "_main_":
    original_car = Car("Toyota", "Camry", "Blue")
    print("Оригинальный автомобиль:", original_car)

    cloned_car = original_car.clone()
    print("Клонированный автомобиль:", cloned_car)

    cloned_car.color = "Red"
    print("Измененный клонированный автомобиль:", cloned_car)

    print("Оригинальный автомобиль (после изменения клонированного):", original_car)
