import pytest

from classes.menu import Menu

def test_create_menu_instance():
    menu = Menu()
    assert menu

def test_add_menu_item_to_non_existent_restaurant():
    menu = Menu()
    with pytest.raises(ValueError):
        menu.add_menu_item("Non-existent Restaurant", "Pepperoni Pizza", "A classic pepperoni pizza", 12.99)

def test_add_menu_item_with_invalid_price():
    menu = Menu()
    with pytest.raises(ValueError):
        menu.add_menu_item("Pizza Palace", "Pepperoni Pizza", "A classic pepperoni pizza", "invalid")

def test_add_duplicate_menu_item():
    menu = Menu()
    menu.add_menu_item("Pizza Palace", "Cheese Pizza", "A classic cheese pizza with a buttery crust", 11.99)
    with pytest.raises(ValueError):
        menu.add_menu_item("Pizza Palace", "Cheese Pizza", "Another classic cheese pizza", 12.99)

def test_get_menu_for_non_existent_restaurant():
    menu = Menu()
    with pytest.raises(ValueError):
        menu.get_menu("Non-existent Restaurant")

def test_update_non_existent_menu_item():
    menu = Menu()
    with pytest.raises(ValueError):
        menu.update_menu_item("Pizza Palace", "Non-existent Item", "New description", 12.99)

def test_update_menu_item_with_invalid_data():
    menu = Menu()
    menu.add_menu_item("Pizza Palace", "Pepperoni Pizza", "A classic pepperoni pizza", 12.99)
    with pytest.raises(ValueError):
        menu.update_menu_item("Pizza Palace", "Pepperoni Pizza", "", -1.0)

def test_delete_non_existent_menu_item():
    menu = Menu()
    with pytest.raises(ValueError):
        menu.delete_menu_item("Pizza Palace", "Non-existent Item")

def test_delete_menu_item_from_non_existent_restaurant():
    menu = Menu()
    with pytest.raises(ValueError):
        menu.delete_menu_item("Non-existent Restaurant", "Pepperoni Pizza")

def test_get_menu_with_no_items():
    menu = Menu()
    menu.restaurant_menus["Pizza Palace"] = []
    assert menu.get_menu("Pizza Palace") == []

def test_add_menu_item_with_overly_long_name():
    menu = Menu()
    name_too_long = "This is a menu item name that is excessively long and should not be allowed."
    with pytest.raises(ValueError):
        menu.add_menu_item("Pizza Palace", name_too_long, "A classic pepperoni pizza", 12.99)

def test_add_menu_item_with_overly_long_description():
    menu = Menu()
    description_too_long = "This is a menu item description that is excessively long and should not be allowed."
    with pytest.raises(ValueError):
        menu.add_menu_item("Pizza Palace", "Pepperoni Pizza", description_too_long, 12.99)
