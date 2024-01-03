import pytest
from classes.restaurant_reviews import RestaurantReviews

@pytest.fixture
def default_restaurant_reviews():
    rr = RestaurantReviews()
    rr.add_review("Default Diner", "Great burgers",5)
    rr.add_review("Permanent Pizza", "Best pizzas for developers", 5)
    rr.add_review("Static Sushi", "Fish was raw !", 1)
    return rr