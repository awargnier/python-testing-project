import pytest

from restaurant_reviews import RestaurantReviews

def test_update_existing_review():
  rr = RestaurantReviews()
  rr.add_review("La Pizza de la mama", "Very good hawai pizza", 4)
  update_result = rr.update_review("La Pizza de la mama", "Pizza not that so good", 2)
  get_result = rr.get_review("La Pizza de la mama")
  assert update_result == "Review added for La Pizza de la mama"
  assert get_result == {'review_text': "Pizza not that so good", 'rating': 2}

def test_update_unexisting_review():
  rr = RestaurantReviews()
  result = rr.update_review("Gros King", "Same Burger at Burger King but very high price", 1)
  assert result == "Review not found"