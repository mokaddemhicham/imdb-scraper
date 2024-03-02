
class Movie:
    def __init__(self, title, year, rating, runtime, link, image):
        self.title = title
        self.year = year
        self.rating = rating
        self.runtime = runtime
        self.link = link
        self.image = image

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.rating} - {self.runtime}'
