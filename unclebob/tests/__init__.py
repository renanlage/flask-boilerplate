import logging

from flask.ext.testing import TestCase

from unclebob.factory import create_app


class FlaskTest(TestCase):
    def create_app(self):
        app = create_app()
        app.logger.setLevel(logging.DEBUG)
        return app
