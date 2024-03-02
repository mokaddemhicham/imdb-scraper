from configurations.database import Database
from models.Movie import Movie
from services.IMDbScraper import IMDbScraper
from tqdm import tqdm
import json
import matplotlib.pyplot as plt
import csv


class MovieManager:
    def __init__(self):
        self.movieService = IMDbScraper()
        self.movies = []
        self.load_movies()
        self.db = Database()

    def create_movie(self, index):
        title = self.movieService.get_title(index)
        year = self.movieService.get_year(index)
        rating = self.movieService.get_rating(index)
        runtime = self.movieService.get_runtime(index)
        link = self.movieService.get_link(index)
        image = self.movieService.get_image(index)
        return Movie(title, year, rating, runtime, link, image)

    def create_movies(self):
        for i in tqdm(range(1, 250 + 1), desc='Scraping Movies', unit='Movie'):
            self.movies.append(self.create_movie(i))

    def get_movie(self, index):
        return self.movies[index]

    def get_movie_count(self):
        return len(self.movies)

    def save_movies_as_json(self):
        with open('./output/movies.json', 'w') as file:
            json.dump([movie.__dict__ for movie in self.movies], file, indent=4)
        print("Movies saved to JSON file successfully!")

    def save_movies_as_csv(self, filename='./output/movies.csv'):
        """
        Save movies to a CSV file.
        """
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Title', 'Year', 'Rating', 'Runtime', 'Link', 'Image'])
                for movie in self.movies:
                    writer.writerow([movie.title, movie.year, movie.rating, movie.runtime, movie.link, movie.image])
            print("Movies saved to CSV file successfully!")
        except Exception as e:
            print("Error while saving movies to CSV:", e)

    def load_movies(self):

        # Load movies from the database if available
        self.retrieve_movies_from_db()

        # If no movies are found in the database, scrape movies from IMDb
        if self.get_movie_count() == 0:
            print('No movies found in the database. Scraping movies from IMDb...')
            self.create_movies()
            print('Movies scraped successfully!')
            self.save_movies_as_json()
            self.save_movies_as_csv()
            self.persist_movies_to_db()
        else:
            print('Movies loaded from database successfully!')

    def persist_movies_to_db(self):

        try:
            self.db = Database()

            query = 'INSERT INTO movies (title, year, rating, runtime, link, image) VALUES (%s, %s, %s, %s, %s, %s)'

            for movie in self.movies:
                movie_data = (movie.title, int(movie.year), float(movie.rating), movie.runtime, movie.link, movie.image)
                self.db.dbcursor.execute(query, movie_data)

            self.db.commit_db()
            print("Movies saved to database successfully!")
        except Exception as e:
            print('Error while connecting to MySQL : ', e)
        finally:
            self.db.close_db()

    def retrieve_movies_from_db(self):
        """
        Retrieves movies from the database.
        """
        try:
            self.db = Database()
            query = "SELECT * FROM movies"
            self.db.dbcursor.execute(query)
            movies_from_db = self.db.dbcursor.fetchall()
            for movie_data in movies_from_db:
                # Create Movie objects from database data
                movie = Movie(movie_data[1], movie_data[2], movie_data[3], movie_data[4], movie_data[5], movie_data[6])
                self.movies.append(movie)
        except Exception as e:
            print("Error while retrieving movies from database:", e)
        finally:
            self.db.close_db()

    def plot_rating_numbers(self):

        ratings = [float(movie.rating) for movie in self.movies]
        plt.hist(ratings, bins=10, edgecolor='black')
        plt.title('Rating Distribution')
        plt.xlabel('Rating')
        plt.ylabel('Count')
        plt.show()
        print("Rating distribution plotted successfully!")

    def search_movies_by_title(self, title):
        """
        Search for movies by title from the database.
        """
        try:
            self.db = Database()
            query = "SELECT * FROM movies WHERE title LIKE %s"
            self.db.dbcursor.execute(query, ('%' + title + '%',))
            movies_from_db = self.db.dbcursor.fetchall()
            movies = []
            for movie_data in movies_from_db:
                # Create Movie objects from database data
                movie = Movie(movie_data[1], movie_data[2], movie_data[3], movie_data[4], movie_data[5], movie_data[6])
                movies.append(movie)
            return movies
        except Exception as e:
            print("Error while searching movies by title:", e)
            return []
        finally:
            self.db.close_db()
