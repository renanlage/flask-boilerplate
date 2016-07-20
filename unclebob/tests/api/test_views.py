# -*- coding: utf-8 -*-

from flask import url_for

from unclebob.tests import FlaskTest


class IndexTest(FlaskTest):
    def test_return_hello_world(self):
        resp = self.client.get(url_for('api.index'))

        self.assertEqual('hello_world', resp.json)
