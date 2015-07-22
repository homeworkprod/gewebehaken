# -*- coding: utf-8 -*-

import json
from unittest import TestCase

from gewebehaken.app import create_app


class AbstractAppTestCase(TestCase):

    def setUp(self):
        app = create_app()
        self.client = app.test_client()

    def post_json(self, path, data):
        return self.client.post(path,
                               content_type='application/json',
                               data=json.dumps(data))

    def assert204(self, result):
        assert result.status_code == 204
        assert result.data == b''


class AbstractHooksTestCase(AbstractAppTestCase):

    def setUp(self):
        super().setUp()
        self.received_signal_data = {}

    def storeReceivedSignalData(self, data):
        self.received_signal_data.update(data)

    def assertReceivedSignalDataEqual(self, expected):
        assert self.received_signal_data == expected
