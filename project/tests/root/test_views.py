from flask import url_for

from project.tests import FlaskTest


class IndexTest(FlaskTest):
    def test_return_hello_world(self):
        resp = self.client.get(url_for('root.index'))

        self.assertEqual({'message': 'Hello world!'}, resp.json)
