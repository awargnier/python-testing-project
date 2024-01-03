import pytest

from classes.restaurant_reviews import RestaurantReviews,ReviewDoesNotExists

@pytest.mark.parametrize("restaurant, expected_output",[
    ("Default Diner", ({'review_text': 'Great burgers', 'rating': 5})),
    ("Permanent Pizza", ({'review_text': 'Best pizzas for developers', 'rating': 5})),
    ("Static Sushi", ({"review_text": "Fish was raw !", "rating": 1}))
])

def test_get_valid_review (restaurant, expected_output, default_restaurant_reviews) :
    rr = default_restaurant_reviews
    assert rr.get_review(restaurant) == expected_output

@pytest.mark.parametrize("restaurant, expected_output",[
    ("Cafe Mocha", "Cafe Mocha does not have review"),
    ("Best Burgers", "Best Burgers does not have review")
])

def test_get_invalid_review (restaurant, expected_output, default_restaurant_reviews) :
    with pytest.raises(ReviewDoesNotExists) as e: 
        rr = default_restaurant_reviews
        rr.get_review(restaurant)
    assert str(e.value) == expected_output