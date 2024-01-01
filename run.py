import os
from app import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')


@app.route("/")
def ping():
    return "Welcome to the entertainment web app"


if __name__ == "__main__":
    app.run()
