import unittest

from flaskr.search_food_items import FoodMenu


class TestSearchFoodItems(unittest.TestCase):

    def test_food_menu_burritos(self):
        food_menu = FoodMenu(item_type='food')
        items = food_menu.search_items('burrito')
        names = [item['name'] for item in items]
        self.assertEqual(type(names), list)
        self.assertEqual(names[0:4], ['7-Layer Burrito', 'Bean Burrito',
                                               'Beefy 5-Layer Burrito', 'Beefy Fritos® Burrito'])

    def test_food_menu_tacos(self):
        food_menu = FoodMenu(item_type='food')
        items = food_menu.search_items('taco')
        names = [item['name'] for item in items]
        self.assertEqual(type(names), list)
        self.assertEqual(names[0:3], ['Breakfast Soft Taco - Bacon',
                                      'Breakfast Soft Taco - Egg & Cheese',
                                      'Breakfast Soft Taco - Sausage'])

    def test_food_menu_chips(self):
        food_menu = FoodMenu(item_type='food')
        items = food_menu.search_items('chips')
        names = [item['name'] for item in items]
        self.assertEqual(type(names), list)
        self.assertEqual(names[0:4], ['Chips and Guacamole',
                                      'Chips and Nacho Cheese Sauce',
                                      'Chips and Pico de Gallo', 'Chips and Salsa'])

    def test_food_menu_drinks_freezes(self):
        food_menu = FoodMenu(item_type='drinks')
        items = food_menu.search_items('freeze')
        names = [item['name'] for item in items]
        self.assertEqual(type(names), list)
        self.assertEqual(names[0:2], ['Crush® Orange Vanilla Float Freeze™ (16 oz)',
                                      'Crush® Orange Vanilla Float Freeze™ (20 oz)'])

    def test_food_menu_drinks_baja_blast(self):
        food_menu = FoodMenu(item_type='drinks')
        items = food_menu.search_items('baja blast')
        names = [item['name'] for item in items]
        self.assertEqual(type(names), list)
        self.assertEqual(names[0:2], ['Diet Mountain Dew® Baja Blast™',
                                      'Mountain Dew® Baja Blast Freeze™ (16 oz)'])

class TestSearchHealthyItem(unittest.TestCase):

    def test_lowest_calories(self):
        food_menu = FoodMenu(item_type='all')
        type = 'taco'
        indicator = 'calories'
        high_low = 'low'
        healthiest_item = food_menu.healthy_item(type, indicator, high_low)
        self.assertEqual(healthiest_item, {'name': 'Fresco Crunchy Taco - Beef', 'cost': 1.19, 'calories': 140, 'caloriesFromFat': 70, 'totalFat': 7, 'saturatedFat': 2, 'transFat': 0, 'cholesterol': 15, 'sodium': 300, 'Carbohydrates': 13, 'dietaryFiber': 3, 'sugars': 1, 'protein': 6})

    def test_highest_calories(self):
        food_menu = FoodMenu(item_type='all')
        type = 'taco'
        indicator = 'calories'
        high_low = 'high'
        healthiest_item = food_menu.healthy_item(type, indicator, high_low)
        self.assertEqual(healthiest_item, {'name': 'Fiesta Taco Salad - Beef', 'cost': 5.19, 'calories': 770, 'caloriesFromFat': 350, 'totalFat': 39, 'saturatedFat': 10, 'transFat': 1, 'cholesterol': 55, 'sodium': 1, 'Carbohydrates': 77, 'dietaryFiber': 11, 'sugars': 8, 'protein': 27})

    def test_highest_calories_drinks(self):
        food_menu = FoodMenu(item_type='drinks')
        type = ''
        indicator = 'calories'
        high_low = 'high'
        healthiest_item = food_menu.healthy_item(type, indicator, high_low)
        print(healthiest_item, {'name': 'Manzanita Sol', 'cost': 1.99, 'calories': 550, 'caloriesFromFat': 0, 'totalFat': 0, 'saturatedFat': 0, 'transFat': 0, 'cholesterol': 0, 'sodium': 125, 'Carbohydrates': 145, 'dietaryFiber': 0, 'sugars': 140, 'protein': 0})

    def test_lowest_calories_drinks(self):
        food_menu = FoodMenu(item_type='drinks')
        type = ''
        indicator = 'calories'
        high_low = 'low'
        healthiest_item = food_menu.healthy_item(type, indicator, high_low)
        print(healthiest_item, {'name': 'Diet Mountain Dew®', 'cost': 1.99, 'calories': 0, 'caloriesFromFat': 0, 'totalFat': 0, 'saturatedFat': 0, 'transFat': 0, 'cholesterol': 0, 'sodium': 80, 'Carbohydrates': 0, 'dietaryFiber': 0, 'sugars': 0, 'protein': 0})


if __name__ == "__main__":
    unittest.main()