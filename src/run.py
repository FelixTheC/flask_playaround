from app import flask_app, register_blueprints

register_blueprints(flask_app)

if __name__ == '__main__':
    flask_app.run()
