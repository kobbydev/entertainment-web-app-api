import os
import cloudinary
import cloudinary.uploader
from app.services import MoviesService

cloudinary.config(cloud_name=os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'),
                  api_secret=os.getenv('API_SECRET'))


class MoviesController:

    @staticmethod
    def add_movie(title, thumbnail_trending_file, thumbnail_regular_file, year, category, rating, is_trending):
        if thumbnail_trending_file:
            uploaded_thumbnail_trending = cloudinary.uploader.upload(thumbnail_trending_file)
            thumbnail_trending = uploaded_thumbnail_trending["secure_url"]
        else:
            thumbnail_trending = thumbnail_trending_file
        if thumbnail_regular_file:
            uploaded_thumbnail_regular = cloudinary.uploader.upload(thumbnail_regular_file)
            thumbnail_regular = uploaded_thumbnail_regular["secure_url"]
        else:
            thumbnail_regular = thumbnail_regular_file

        movie = MoviesService.add_movie(title, thumbnail_trending, thumbnail_regular, year, category,
                                        rating, is_trending)
        return movie
