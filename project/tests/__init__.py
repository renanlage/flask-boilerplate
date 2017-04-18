import logging

from flask_testing import TestCase

from project.factory import create_app


class FlaskTest(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.logger.setLevel(logging.DEBUG)
        return app
