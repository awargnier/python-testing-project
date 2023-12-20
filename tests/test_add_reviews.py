import pytest

from restaurant_reviews import RestaurantReviews, InvalidRatingError

def test_add_valide_review():
  rr = RestaurantReviews() 
  result = rr.add_review("Cafe Mocha", "Great coffee and pastries", 4)
  assert result == "Review added for Cafe Mocha"
  assert rr.get_review("Cafe Mocha") == {'review_text' : "Great coffee and pastries", 'rating': 4}

def test_add_invalide_rating():
  rr = RestaurantReviews()
  with pytest.raises(InvalidRatingError) as excinfo:
    rr.add_review("Cafe Mocha", "Good ambiance", 6)
  assert str(excinfo.value) == "It must be between 1 and 5"
