import pytest

from restaurant_reviews import RestaurantReviews

def test_get_existing_review():
  rr = RestaurantReviews()
  rr.add_review("Une ptite biere ?", "Greatest beer i never drink", 5)
  result = rr.get_review("Une ptite biere ?")
  assert result == {'review_text' : "Greatest beer i never drink", 'rating': 5}

def test_get_unexisting_review():
  rr = RestaurantReviews()
  result = rr.get_review("Le genie")
  assert result == "Review not found"