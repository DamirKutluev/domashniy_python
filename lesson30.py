##########################__ЗАДАНИЕ_1__########################################
class Shoes:
    def __init__(
        self, shoe_type, view_shoe, color_shoe, price_shoe, brand_shoe, size_shoe
    ):
        self.shoe_type = shoe_type
        self.view_shoe = view_shoe
        self.color_shoe = color_shoe
        self.price_shoe = price_shoe
        self.brand_shoe = brand_shoe
        self.size_shoe = size_shoe


class ModelShoe:
    def __init__(self):
        self.shoe = []

    def add_shoe(self, shoe):
        self.shoe.append(shoe)

    def get_shoe(self):
        return self.shoe


class ControllerShoe:
    def __init__(self, model):
        self.model = model

    def add_shoe(
        self, shoe_type, view_shoe, color_shoe, price_shoe, brand_shoe, size_shoe
    ):
        shoe = Shoes(
            shoe_type, view_shoe, color_shoe, price_shoe, brand_shoe, size_shoe
        )
        self.model.add_shoe(shoe)

    def get_shoe(self):
        return self.model.get_shoe()


class PerformanceShoe:
    def show_shoe(self, shoe):
        for unit_shoe in shoe:
            print(
                f"Модель:\n"
                f"Тип: {unit_shoe.shoe_type}, Вид: {unit_shoe.view_shoe}, Цвет: {unit_shoe.color_shoe},\n "
                f"Цена: {unit_shoe.price_shoe}, Производитель: {unit_shoe.brand_shoe}, Размер: {unit_shoe.size_shoe}"
            )


model = ModelShoe()
controller = ControllerShoe(model)
performance = PerformanceShoe()
all_shoes = controller.get_shoe()


def main():
    while True:
        print("Добро пожаловать!\n" "Выберите из предложенного, что хотите сделать.")
        print("1 - добавить обувь")
        print("2 - посмотреть список добавленной обуви")
        print("3 - выйти")
        choice = input("--->")
        if choice == "1":
            type = input("Введите тип обуви (мужская/женская): ")
            view = input(
                "Введите вид обуви (кроссовки, сапоги, сандалии, туфли и т.д.): "
            )
            color = input("Введите цвет: ")
            price = int(input("Введите цену: "))
            brand = input("Введите производителя: ")
            size = int(input("Введите размер: "))
            controller.add_shoe(type, view, color, price, brand, size)
        elif choice == "2":
            print(performance.show_shoe(all_shoes))
        elif choice == "3":
            break
        else:
            print("Такого выбора в предложенном нет!")


##########################__ЗАДАНИЕ_2__########################################
class Recipe:
    def __init__(
        self,
        name_recipe,
        after_recipe,
        type_recipe,
        list_ingredients,
        name_kitchen,
        recipe_description,
        link_video,
    ):
        self.name_recipe = name_recipe
        self.after_recipe = after_recipe
        self.type_recipe = type_recipe
        self.list_ingredients = list_ingredients
        self.name_kitchen = name_kitchen
        self.recipe_description = recipe_description
        self.link_video = link_video


class ModelRecipe:
    def __init__(self):
        self.recipe = []

    def add_recipe(self, recipe):
        self.recipe.append(recipe)

    def get_recipe(self):
        return self.recipe


class ControllerRecipe:
    def __init__(self, model):
        self.model = model

    def add_recipe(
        self,
        name_recipe,
        after_recipe,
        type_recipe,
        list_ingredients,
        name_kitchen,
        recipe_description,
        link_video,
    ):
        recipe = Recipe(
            name_recipe,
            after_recipe,
            type_recipe,
            list_ingredients,
            name_kitchen,
            recipe_description,
            link_video,
        )
        self.model.add_recipe(recipe)

    def get_recipe(self):
        return self.model.get_recipe()


class PerformanceRecipe:
    def show_recipe(self, recipe):
        for unit in recipe:
            print(
                f"Рецепт:\n"
                f"Название:{unit.name_recipe}, Автор:{unit.after_recipe}, Тип:{unit.type_recipe}, Название кухни:{unit.name_kitchen}\n"
                f"Список ингредиентов:{unit.list_ingredients},\n"
                f"Описание рецепта:{unit.recipe_description}\n"
                f"Ссылка на видео с рецептом:{unit.link_video}"
            )


modell = ModelRecipe()
controllerr = ControllerRecipe(modell)
performancee = PerformanceRecipe()
all_recipe = controllerr.get_recipe()


def mainn():
    while True:
        print("Добро пожаловать!\n" "Выберите из предложенного, что хотите сделать.")
        print("1 - добавить рецепт")
        print("2 - посмотреть список добавленных рецептов")
        print("3 - выйти")
        choice = input("--->")
        if choice == "1":
            name_recipe = input("Введите названеие рецепта: ")
            after = input("Введите автора рецепта: ")
            type_recipe = input("Введите тип рецепта (первое, второе блюдо и т.д.): ")
            name_kitchen = input(
                "Введите название кухни и (итальянская, французская и т.д.): "
            )
            list = input("Введите список ингредиентов через запятую: ")
            description = input("Введите текстовое описание рецепта: ")
            link = input("Введите ссылку на видео с рецептом: ")
            controllerr.add_recipe(
                name_recipe, after, type_recipe, name_kitchen, list, description, link
            )
        elif choice == "2":
            print(performancee.show_recipe(all_recipe))
        elif choice == "3":
            break
        else:
            print("Такого выбора в предложенном нет!")


def start():
    while True:
        print("выбирете к чему перейти.")
        print("1 - обувь.")
        print("2 - рецепты.")
        print("3 - завершить.")
        num = input("--->")
        if num == "1":
            main()
        elif num == "2":
            mainn()
        elif num == "3":
            break
        else:
            print("Такого выбора нет!")


start()
