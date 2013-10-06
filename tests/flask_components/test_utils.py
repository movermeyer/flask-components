# -*- coding: utf-8 -*-
from flask.ext import components
from flask import Flask


class TestFind:

    def test_config(self):
        app = Flask('components')
        app.config['COMPONENTS'] = ['flask', 'jinja2']
        items = components.find('ext', app)

        assert len(items) == 2

    def test_context_config(self):
        app = Flask('components')
        app.config['COMPONENTS'] = ['flask', 'jinja2']
        with app.app_context():
            items = components.find('ext')

        assert len(items) == 2

    def test_find_in_module_and_package(self):
        items = components.find('ext', components=['flask', 'jinja2'])

        assert len(items) == 2

    def test_find_normalize(self):
        items = components.find('ext', components=['flask', 'jinja2'])

        assert len(items) == 2
        assert 'Extension' in items[1]

    def test_find_normalize_limit(self):
        items = components.find(
            'utils', components=['jinja2', 'flask.ext.components'])

        assert len(items) == 2
        assert 'find' in items[1]
        assert 'import_module' not in items[1]

    def test_find_nothing(self):
        items = components.find('foo', components=['flask_components'])

        assert len(items) == 0
