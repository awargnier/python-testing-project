import pytest

from classes.restaurant_reviews import RestaurantReviews,ReviewDoesNotExists

def test_delete_valid_review () :
    rr=RestaurantReviews()
    rr.reviews["Cafe Mocha"] = {'review_text':"Great coffee and pastries", 'rating':5}
    rr.delete_review('Cafe Mocha')
    assert rr.reviews == {}

def test_delete_invalid_review () :
    with pytest.raises(ReviewDoesNotExists) as e :
        rr=RestaurantReviews()
        rr.delete_review('Cafe Mocha')
    assert str(e.value) == "Cafe Mocha does not have review"