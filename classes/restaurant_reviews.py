class ReviewAlreadyExists (Exception) :
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ReviewDoesNotExists (Exception) :
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class RestaurantReviews:
  def __init__(self):
    self.reviews = {}
  
  def add_review(self,restaurant, review_text, rating):
    if rating<0 or rating>5 : raise ValueError(f"rating must be between 0 and 5 (given: {rating})")
    if restaurant in self.reviews.keys()  : raise ReviewAlreadyExists(restaurant+" already has a review")
    review={"review_text":review_text, "rating":rating}
    self.reviews[restaurant]=review
    return review
  
  def get_review(self, restaurant):
    if not restaurant in self.reviews.keys() : raise ReviewDoesNotExists(restaurant + " does not have review")
    return self.reviews[restaurant]

  def update_review(self, restaurant, new_review_text, new_rating):
    if not restaurant in self.reviews.keys() : raise ReviewDoesNotExists(restaurant + " does not have review")
    if new_rating<0 or new_rating>5 : raise ValueError(f"rating must be between 0 and 5 (given: {new_rating})")
    review={"review_text":new_review_text, "rating":new_rating}
    self.reviews[restaurant]=review
    return review
  
  def delete_review(self, restaurant):
    if not restaurant in self.reviews.keys() : raise ReviewDoesNotExists(restaurant + " does not have review")
    return self.reviews.pop(restaurant)
