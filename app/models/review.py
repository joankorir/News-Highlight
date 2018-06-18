clas Review:

   all_reviews = []

   def __init__(self,newsHighlight_id,title,imageurl,review):
       self.newsHighlight_id = newsHighlight_id
       self.title = title
       self.imageurl = imageurl
       self.review = review


    def save_review(self):
        Review.all_reviews.append(self)



    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()