from app import create_app, setup_database
from flask import render_template


def add_vue_routes(app):
    @app.route('/')
    def serve_vue_app():
        return(render_template('index.html'))

    @app.after_request
    def add_header(req):
        req.headers['Cache-Control'] = "no-cache"
        return req


if __name__ == '__main__':
    app = create_app()
    add_vue_routes(app)
    setup_database(app)
    app.run(debug=True)
