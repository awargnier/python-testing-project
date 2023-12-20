class InvalidRatingError(Exception):
  """Exception raised for errors in the rating"""
  pass
class ReviewNotFoundError(Exception):
  """Exception raised when a review is not found"""
  pass


class RestaurantReviews:
  def __init__(self):
    self.reviews = {}
  
  def add_review(self,restaurant, review_text, rating):
    if(rating < 1 or rating > 5):
      raise InvalidRatingError("It must be between 1 and 5")
    self.reviews[restaurant] = {'review_text': review_text, 'rating': rating}
    return f"Review added for {restaurant}"
  
  def get_review(self, restaurant):
    if(restaurant not in self.reviews):
      raise ReviewNotFoundError("Review not found")
    return self.reviews[restaurant]

  def update_review(self, restaurant, new_review_text, new_rating):
    if(restaurant not in self.reviews):
      raise ReviewNotFoundError("Review not found")
    return self.add_review(restaurant, new_review_text, new_rating)
  
  def delete_review(self, restaurant):
    if(restaurant not in self.reviews):
      raise ReviewNotFoundError("Review not found")
    del self.reviews[restaurant]
    return f"Review deleted for {restaurant}"

    