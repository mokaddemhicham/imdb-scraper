# IMDb Scraper Project

## Purpose
The IMDb Scraper Project is a Python application designed to scrape movie data from IMDb's top-rated movies list and store it in various formats such as CSV, JSON, and a MySQL database. It provides functionalities to retrieve movie details, search for movies, and analyze rating distributions.

## Installation
To install the required dependencies for this project, run the following command in your terminal:

```bash
pip install -r utilities/requirements.txt
```

The requirements.txt file includes the following dependencies:

- beautifulsoup4==4.12.3
- requests==2.31.0
- matplotlib==3.8.3
- lxml==5.1.0
- flask==3.0.2
- pymysql==1.1.0
- configparser==6.0.1

Ensure you have Python and pip installed on your system before running the installation command.

## Usage

To use the IMDb Scraper Project, you have a couple of options:

1. **Run the Main Script**:

You can execute the `main.py` script situated in the project's root directory. This script initializes the `MovieManager` and offers functionalities to handle movie data.

```bash
python main.py
```
2. **Run the REST API Endpoints**:

If you prefer to interact with the project via REST API, you can run the `MovieController.py` script located in the `controllers` folder. This will activate the REST API endpoints, allowing you to perform operations such as retrieving movie information, searching for movies, and obtaining movie counts.

```bash
python controllers/MovieController.py
```

## Files and Directories
- **models/**: Contains the Python class definitions for the Movie object.
- **services/**: Contains the Python modules for scraping movie data from IMDb and managing movies.
- **configurations/**: Includes configuration files and database setup.
- **utilities/**: Contains utility files such as xpaths.txt and requirements.txt.
- **output/**: Directory where the scraped movie data is saved in CSV and JSON formats.
- **controllers/**: Contains Flask API controllers for accessing movie data.
- **main.py**: Main script to run the movie scraper application.
- **movies_db.sql**: SQL script to create the movies table in the MySQL database.
- **README.md**: This file provides an overview of the project and instructions for installation and usage.

## Collaboration

I welcome contributions and collaboration on the IMDb Scraper Project. Here are a few ways you can contribute:

- **Code Contributions**: If you find any bugs or issues, feel free to open a GitHub issue or submit a pull request with your fixes or enhancements.
- **Feature Requests**: If you have any ideas for new features or improvements, please share them by opening a GitHub issue.
- **Documentation Improvements**: Help improve the project's documentation by suggesting edits, clarifications, or additional examples.
- **Spread the Word**: Share the project with others who might find it useful, and consider giving it a star on GitHub to show your support.

Let's collaborate and make the IMDb Scraper Project even better!
