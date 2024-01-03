import pytest

from classes.restaurant_reviews import RestaurantReviews, ReviewAlreadyExists

def test_add_valid_review () :
    rr = RestaurantReviews()
    rr.add_review("Cafe Mocha", "Great coffee and pastries",5)
    assert rr.reviews["Cafe Mocha"] == {'review_text':"Great coffee and pastries", 'rating':5}

def test_add_invalid_review () :
    with pytest.raises(ValueError) as e: #invalid rating
        rr = RestaurantReviews()
        rr.add_review("Cafe Mocha", "Worst coffe ever!", -99)
    assert str(e.value) == "rating must be between 0 and 5 (given: -99)"
    with pytest.raises(ReviewAlreadyExists) as e: #review already exists
        rr = RestaurantReviews()
        rr.add_review("Cafe Mocha", "Great coffee and pastries",5)
        rr.add_review("Cafe Mocha", "Great coffee and pastries",5)
    assert str(e.value) == "Cafe Mocha already has a review"
