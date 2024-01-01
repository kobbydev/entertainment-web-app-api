from flask import request, Blueprint, current_app
from app.controllers import MoviesController


movies_bp = Blueprint("movies", __name__)


@movies_bp.route("/add_movie", methods=["POST"])
def add_movie():
    thumbnail_regular_file = request.files.get("thumbnail_regular", "")
    thumbnail_trending_file = request.files.get("thumbnail_trending", "")
    title = request.form.get("title")
    category = request.form.get("category")
    year = request.form.get("release_year")
    is_trending = request.form.get("is_trending")
    rating = request.form.get("rating")
    try:
        movie = MoviesController.add_movie(title, thumbnail_trending_file, thumbnail_regular_file, year, category,
                                           rating, is_trending)
        current_app.logger.info('Movie created successfully')
        return {"message": "Movie created successfully", "data": movie}, 201
    except Exception as e:
        current_app.logger.error(e)
        return {"message": "Error while processing, it's not you it's us"}, 500
    # if movie:
    #     return {"message": "Movie created successfully", "data": movie}, 201
    # return {"message": "Error occurred"}, 500
