import pytest

from restaurant_reviews import RestaurantReviews,ReviewNotFoundError

def test_delete_existing_review():
  rr = RestaurantReviews()
  rr.add_review("Gros King", "Same Burger at Burger King but very high price", 1)
  delete_result = rr.delete_review("Gros King")
  assert delete_result == "Review deleted for Gros King"
  with pytest.raises(ReviewNotFoundError) as excinfo:
    rr.get_review("Gros King")
  assert str(excinfo.value) == "Review not found"

def test_delete_unexisting_review():
  rr = RestaurantReviews()
  with pytest.raises(ReviewNotFoundError) as excinfo:
    rr.delete_review("Gros King")
  assert str(excinfo.value) == "Review not found"