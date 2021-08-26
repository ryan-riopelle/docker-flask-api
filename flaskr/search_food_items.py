import os
import json
import logging

logger = logging.getLogger(__name__)

# typically this data would come from settings or config file
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALL_FOOD_MENU = PROJECT_ROOT + '/menu/all.json'
FOOD_MENU = PROJECT_ROOT + '/menu/food.json'
DRINK_MENU = PROJECT_ROOT + '/menu/drinks.json'

def get_food_menu(item_type):

    if item_type == "food":
        file = FOOD_MENU
    elif item_type == "drinks":
        file = DRINK_MENU
    else:
        file = ALL_FOOD_MENU

    logger.info(f"getting data for {item_type}")

    with open(file) as f:
        data = json.load(f)
    return data

class FoodMenu(object):

    def __init__(self, item_type):
        self.item_type = item_type
        self.food_menu = get_food_menu(item_type)

    def search_items(self, keyword_search: str, names_only: bool = False) -> list:
        item_resp = []
        for item in self.food_menu:
            if keyword_search.lower() in item['name'].lower():
                item_resp.append(item)
        if not names_only:
            return item_resp
        names = [item['name'] for item in item_resp]
        return names

    def healthy_item(self, keyword_search: str, indicator: str, high_low: str):
        """
        Indicator: choose from "calories", "totalFat", "saturatedFat", "transFat"
                    "cholesterol", "sodium", "Carbohydrates", "sugars", or "protein"
        """
        items_found = self.search_items(keyword_search)
        if high_low == 'high':
            return max(items_found, key=lambda x: x[indicator])
        return min(items_found, key=lambda x: x[indicator])


