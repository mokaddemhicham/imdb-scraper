from flask import Flask, jsonify, request
from services.MovieManager import MovieManager

app = Flask(__name__)
service = MovieManager()


@app.route('/movies', methods=['GET'])
def get_movies():
    """
    Endpoint to retrieve all movies.
    """
    movies = [movie.__dict__ for movie in service.movies]
    return jsonify(movies)


@app.route('/movies/<int:index>', methods=['GET'])
def get_movie(index):
    """
    Endpoint to retrieve a specific movie by its index.
    """
    if index < 1 or index > len(service.movies):
        return jsonify({'error': 'Movie index out of range'}), 404

    movie = service.movies[index - 1].__dict__
    return jsonify(movie)


@app.route('/movies/count', methods=['GET'])
def get_movie_count():
    """
    Endpoint to retrieve the total count of movies.
    """
    count = service.get_movie_count()
    return jsonify({'Number of Movies': count})


@app.route('/search', methods=['GET'])
def search_movies():
    """
    Endpoint to search for movies by title.
    """
    try:
        title = request.args.get('title')
        if not title:
            return jsonify({'error': 'Title parameter is missing'}), 400

        search_result = service.search_movies_by_title(title)
        if search_result:
            movies_data = [movie.__dict__ for movie in search_result]
            return jsonify(movies_data), 200
        else:
            return jsonify({'message': 'No movies found with the given title'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
