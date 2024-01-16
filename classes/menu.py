class Menu:

    def __init__(self):
        self.restaurant_menus = {}

    def add_menu_item(self, restaurant_name, item_name, description, price):
        if restaurant_name not in self.restaurant_menus.keys():
            raise ValueError(f"Restaurant with name '{restaurant_name}' does not exist.")

        if price < 0 or not isinstance(price, float):
            raise ValueError(f"Invalid price '{price}' for menu item.")

        if item_name in self.restaurant_menus[restaurant_name]:
            raise ValueError(f"Menu item with name '{item_name}' already exists for restaurant '{restaurant_name}'.")

        self.restaurant_menus[restaurant_name].append({
            "item_name": item_name,
            "description": description,
            "price": price
        })
        return f"Menu item '{item_name}' added successfully to restaurant '{restaurant_name}'."

    def get_menu(self, restaurant_name):
        if restaurant_name not in self.restaurant_menus.keys():
            raise ValueError(f"Restaurant with name '{restaurant_name}' does not exist.")

        return self.restaurant_menus[restaurant_name]

    def update_menu_item(self, restaurant_name, item_name, new_description, new_price):
        if restaurant_name not in self.restaurant_menus.keys():
            raise ValueError(f"Restaurant with name '{restaurant_name}' does not exist.")

        if item_name not in self.restaurant_menus[restaurant_name]:
            raise ValueError(f"Menu item with name '{item_name}' does not exist for restaurant '{restaurant_name}'.")

        if new_price < 0 or not isinstance(new_price, float):
            raise ValueError(f"Invalid price '{new_price}' for menu item.")

        menu_item = self.restaurant_menus[restaurant_name][item_name]
        menu_item.update({
            "description": new_description,
            "price": new_price
        })
        return f"Menu item '{item_name}' updated successfully in restaurant '{restaurant_name}'."

    def delete_menu_item(self, restaurant_name, item_name):
        if restaurant_name not in self.restaurant_menus.keys():
            raise ValueError(f"Restaurant with name '{restaurant_name}' does not exist.")

        if item_name not in self.restaurant_menus[restaurant_name]:
            raise ValueError(f"Menu item with name '{item_name}' does not exist for restaurant '{restaurant_name}'.")

        del self.restaurant_menus[restaurant_name][item_name]
        return f"Menu item '{item_name}' deleted successfully from restaurant '{restaurant_name}'."
