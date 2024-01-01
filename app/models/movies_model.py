INSERT_INTO_MOVIES = """INSERT INTO movies (title, thumbnail_trending, thumbnail_regular,
 release_year, category, rating, is_trending)
VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id, title, thumbnail_trending, thumbnail_regular, 
release_year, category, rating, is_trending;"""
GET_ALL_MOVIES = """SELECT * FROM movies WHERE category = 'Movie';"""
GET_ALL_TV_SHOWS = """SELECT * FROM movies WHERE category = 'Tv Series';"""
GET_SEARCHED_ITEM = """SELECT * FROM movies WHERE title = %s;"""
