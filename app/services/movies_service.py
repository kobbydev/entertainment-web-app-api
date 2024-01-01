import os
import psycopg2
from dotenv import load_dotenv
from app.models import INSERT_INTO_MOVIES

load_dotenv()
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)


class MoviesService:

    @staticmethod
    def add_movie(title, thumbnail_trending, thumbnail_regular, year, category, rating, is_trending):
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(INSERT_INTO_MOVIES, (title, thumbnail_trending, thumbnail_regular, year, category,
                                                    rating, is_trending,))
                movie = cursor.fetchone()

        return {"id": movie[0], "title": movie[1], "thumbnail_trending": movie[2], "thumbnail_regular": movie[3],
                "year": movie[4], "category": movie[5], "rating": movie[6], "is_trending": movie[7]}
