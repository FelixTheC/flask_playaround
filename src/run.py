from app import flask_app
from app import register_blueprints
from app import setup_db

register_blueprints(flask_app)
setup_db()

if __name__ == '__main__':
    flask_app.run()
