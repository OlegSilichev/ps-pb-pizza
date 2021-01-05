class Title:
    """Базовый класс отвечающий за названия. 
    Проверяет обязательный атрибут title. 
    Не может быть пустым""" 

    def __init__(self, title):
        if Title.chek_title(title):
            self.__title = title
        else:
            raise ValueError("Название не может быть пустым")

    # Проверка на заполненность атрибута title при создании экземпляра класса    
    @staticmethod
    def chek_title(title):
        if title:
            return True
        else:
            return False  
    
    # Проверка на заполненность при изменении атрибута title у экземпляра класса
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if len(title) > 0:
            self.__title = title
        else:
            raise ValueError("Название не может быть пустым")
      
      
class Product(Title):
    """ Класс содержащий описание продукта"""

    def __init__(self, title, calorific, cost):
        super().__init__(title)
        if Product.check_calorific_cost(calorific, cost):
            self.calorific = calorific
            self.cost = cost
        else:
            raise ValueError("Значение должно быть только положительным")
    
    # Проверка на положительность значений
    @staticmethod
    def check_calorific_cost(calorific, cost):
        if calorific > 0 and cost >0:
            return True
        else:
            return False
             
class Ingredient:
    """ Класс содержащий описание ингредиента.
        Формируется из продуктов и веса."""

    def __init__(self, Product, weight):
        self.product = Product
        if Ingredient.check_weight(weight):
            self.weight = weight
        else:
            raise ValueError("Значение должно быть только положительным")  

    # Проверка на положительность значений
    @staticmethod
    def check_weight(weight):
        if weight > 0:
            return True
        else:
            return False
    
    def __str__(self):
        return self.product.title

    # Расчет калорийности для ингредиента
    @property
    def get_caloric(self):
        return (self.weight / 100) * self.product.calorific

    # Расчет себестоимости для ингредиента
    @property
    def get_cost(self):
        return (self.weight / 100) * self.product.cost
    
class Pizza(Title):
    """ Класс содержащий описание пиццы.
        Формируется из ингредиентов."""

    def __init__(self, title, Ingredient):
        super().__init__(title)
        self.ingredients = Ingredient

      
    # Расчет калорийности для пиццы
    def get_caloric(self):
        sum_ingredients = 0
        for i in self.ingredients:
           sum_ingredients += i.get_caloric
        return sum_ingredients

    # Расчет себестоимости для пиццы
    def get_cost(self):
        sum_cost = 0
        for i in self.ingredients:
            sum_cost += i.get_cost
        return sum_cost

    def __str__(self):
        return f'{self.title} ({Pizza.get_caloric(self)} kkal) - {Pizza.get_cost(self)} р'
         

# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты. Для каждого ингредиента указываем продукт, 
# из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])


# Выводим экземпляр пиццы
print(pizza_margarita)