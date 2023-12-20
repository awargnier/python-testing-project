import pytest

from restaurant_reviews import RestaurantReviews

def test_delete_existing_review():
  rr = RestaurantReviews()
  rr.add_review("Gros King", "Same Burger at Burger King but very high price", 1)
  delete_result = rr.delete_review("Gros King")
  get_result = rr.get_review("Gros King")
  assert delete_result == "Review deleted for Gros King"
  assert get_result == "Review not found"

def test_delete_unexisting_review():
  rr = RestaurantReviews()
  result = rr.delete_review("Gros King")
  assert result == "Review not found"