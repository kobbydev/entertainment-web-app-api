CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, 
firstname TEXT, lastname TEXT, email TEXT, password TEXT);"""
INSERT_INTO_USER = """INSERT INTO users (firstname, lastname, email, password) 
VALUES (%s, %s, %s, %s) RETURNING id, firstname, lastname, email;"""
FIND_USER_BY_EMAIL = """SELECT id, firstname, lastname, email FROM users WHERE email = %s;"""
FETCH_USER = """SELECT * FROM users WHERE email = %s;"""
